"""
notifiers.py - sending alerts to the flat owner.

  Abstraction  : Notifier says WHAT a channel must do (send), not HOW
  Polymorphism : TelegramNotifier and TwilioSMSNotifier are used the same way
  Composition  : NotificationService HAS a list of Notifiers and a log store

To add a new channel (Email, WhatsApp...) write one more Notifier subclass
and add it to the list in app.py. Nothing else changes.
"""
import threading
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

import requests

from models import TIME_FORMAT


class DeliveryResult:
    def __init__(self, channel, label, ok, detail=""):
        self.channel, self.label, self.ok, self.detail = channel, label, ok, detail

    def to_dict(self):
        return {"channel": self.channel, "label": self.label, "ok": self.ok, "detail": self.detail}


class Notifier(ABC):
    channel = "generic"
    label = "Generic"

    @property
    @abstractmethod
    def enabled(self):
        """True when this channel has all the settings it needs."""

    @abstractmethod
    def status_text(self):
        """Short text for the UI."""

    @abstractmethod
    def send(self, resident, message):
        """Deliver `message` to `resident`. Must return a DeliveryResult."""


class TelegramNotifier(Notifier):
    channel = "telegram"
    label = "Telegram"

    def __init__(self, token):
        self.token = token
        self._username = None

    @property
    def enabled(self):
        return bool(self.token)

    def status_text(self):
        return "Ready" if self.enabled else "Not configured"

    def _call(self, method, **params):
        url = f"https://api.telegram.org/bot{self.token}/{method}"
        response = requests.post(url, data=params, timeout=8)
        data = response.json()
        if not data.get("ok"):
            raise RuntimeError(data.get("description", "Telegram error"))
        return data["result"]

    def send(self, resident, message):
        if not resident.telegram_chat_id:
            return DeliveryResult(self.channel, self.label, False, "Owner has not linked Telegram yet")
        try:
            self._call("sendMessage", chat_id=resident.telegram_chat_id, text=message)
            return DeliveryResult(self.channel, self.label, True, "Delivered")
        except Exception as e:
            return DeliveryResult(self.channel, self.label, False, str(e))

    def send_text(self, chat_id, text):
        try:
            self._call("sendMessage", chat_id=chat_id, text=text)
        except Exception:
            pass

    def bot_username(self):
        if self._username is None:
            self._username = self._call("getMe").get("username", "")
        return self._username

    def fetch_start_requests(self):
        """
        Owners open  t.me/<bot>?start=<flat>  and press Start.
        Telegram then gives us '/start <flat>' plus their chat id.
        Returns a list of (flat_no, chat_id, first_name).
        """
        found = []
        for update in self._call("getUpdates"):
            msg = update.get("message") or {}
            text = (msg.get("text") or "").strip()
            if not text.startswith("/start"):
                continue
            parts = text.split(maxsplit=1)
            if len(parts) < 2:
                continue
            chat = msg.get("chat", {})
            found.append((parts[1].strip().upper(), str(chat.get("id")), chat.get("first_name", "")))
        return found


class TwilioSMSNotifier(Notifier):
    channel = "sms"
    label = "SMS"

    def __init__(self, account_sid, auth_token, from_number, country_code="+91"):
        self.sid, self.token = account_sid, auth_token
        self.from_number, self.country_code = from_number, country_code

    @property
    def enabled(self):
        return bool(self.sid and self.token and self.from_number)

    def status_text(self):
        return "Ready" if self.enabled else "Not configured"

    def send(self, resident, message):
        to = resident.phone if resident.phone.startswith("+") else self.country_code + resident.phone
        url = f"https://api.twilio.com/2010-04-01/Accounts/{self.sid}/Messages.json"
        try:
            r = requests.post(url, data={"To": to, "From": self.from_number, "Body": message},
                              auth=(self.sid, self.token), timeout=10)
            if r.status_code in (200, 201):
                return DeliveryResult(self.channel, self.label, True, "Accepted by Twilio")
            try:
                reason = r.json().get("message", f"HTTP {r.status_code}")
            except ValueError:
                reason = f"HTTP {r.status_code}"
            return DeliveryResult(self.channel, self.label, False, reason)
        except Exception as e:
            return DeliveryResult(self.channel, self.label, False, str(e))


class NotificationService:
    """Sends one message through every enabled channel and keeps a log of it."""

    def __init__(self, notifiers, store, keep=500):
        self.notifiers = notifiers
        self.store = store
        self.keep = keep
        self._lock = threading.RLock()

    def channel_status(self):
        return [{"channel": n.channel, "label": n.label, "enabled": n.enabled, "text": n.status_text()}
                for n in self.notifiers]

    def notify(self, flat, event, message):
        results = self._dispatch(flat.owner, message)
        now = datetime.now()
        record = {
            "id": now.strftime("%Y%m%d%H%M%S%f"),
            "time": now.strftime(TIME_FORMAT),
            "event": event,
            "flat_no": flat.number,
            "owner_name": flat.owner.name,
            "owner_phone": flat.owner.phone,
            "message": message,
            "results": [r.to_dict() for r in results],
        }
        with self._lock:
            items = self.store.read()
            items.append(record)
            self.store.write(items[-self.keep:])
        print(f"[NOTIFY {event}] Flat {flat.number} -> {flat.owner.name}: {message} "
              f"| {[(r.label, r.ok) for r in results] or 'in-app only'}")
        return record

    def recent(self, flat_no=None, limit=100):
        items = self.store.read()
        if flat_no:
            items = [i for i in items if i["flat_no"] == flat_no]
        return list(reversed(items))[:limit]

    def count_today(self):
        today = datetime.now().strftime("%Y-%m-%d")
        return sum(1 for i in self.store.read() if i["time"].startswith(today))

    def _dispatch(self, resident, message):
        active = [n for n in self.notifiers if n.enabled]
        if not active:
            return []
        with ThreadPoolExecutor(max_workers=len(active)) as pool:  # channels send in parallel
            futures = [pool.submit(self._safe_send, n, resident, message) for n in active]
            return [f.result() for f in futures]

    @staticmethod
    def _safe_send(notifier, resident, message):
        try:
            return notifier.send(resident, message)
        except Exception as e:  # one broken channel must never block the others
            return DeliveryResult(notifier.channel, notifier.label, False, str(e))
