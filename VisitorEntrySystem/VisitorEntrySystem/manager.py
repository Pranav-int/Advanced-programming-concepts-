"""
manager.py - the brain of the system.

  FlatRegistry   : keeps the list of flats and their owners
  VisitorManager : check-in / check-out rules, statistics, and notifications
"""
import threading
from datetime import datetime

from models import Flat, Resident, VisitLog


class FlatRegistry:
    SEED = [
        ("101", "Mr. Sharma", "9876543210"),
        ("102", "Mrs. Patil", "9123456780"),
        ("201", "Mr. Khan", "9988776655"),
        ("202", "Ms. Joshi", "9012345678"),
    ]

    def __init__(self, store):
        self.store = store
        self._lock = threading.RLock()
        data = store.read()
        if data:
            self._flats = {d["number"]: Flat.from_dict(d) for d in data}
        else:  # first run: sample data so the app is not empty
            self._flats = {n: Flat(n, Resident(name, phone)) for n, name, phone in self.SEED}
            self._save()

    @staticmethod
    def _key(number):
        return (number or "").strip().upper()

    def all(self):
        return sorted(self._flats.values(), key=lambda f: (len(f.number), f.number))

    def get(self, number):
        return self._flats.get(self._key(number))

    def add(self, number, owner_name, owner_phone):
        with self._lock:
            flat = Flat(number, Resident(owner_name, owner_phone))  # validates everything
            if flat.number in self._flats:
                raise ValueError(f"Flat {flat.number} already exists.")
            self._flats[flat.number] = flat
            self._save()
            return flat

    def update(self, number, owner_name, owner_phone, unlink_telegram=False):
        with self._lock:
            flat = self._need(number)
            chat_id = None if unlink_telegram else flat.owner.telegram_chat_id
            flat.owner = Resident(owner_name, owner_phone, chat_id)  # validates before replacing
            self._save()
            return flat

    def link_telegram(self, number, chat_id):
        with self._lock:
            self._need(number).owner.telegram_chat_id = chat_id
            self._save()

    def remove(self, number):
        with self._lock:
            self._need(number)
            del self._flats[self._key(number)]
            self._save()

    def _need(self, number):
        flat = self.get(number)
        if flat is None:
            raise ValueError(f"Flat {number} does not exist.")
        return flat

    def _save(self):
        self.store.write([f.to_dict() for f in self._flats.values()])


class VisitorManager:
    def __init__(self, registry, notifications, store, society_name="Residency"):
        self.registry = registry
        self.notifications = notifications
        self.store = store
        self.society = society_name
        self._lock = threading.RLock()
        self.logs = [VisitLog.from_dict(d) for d in store.read()]

    # ---------------------------------------------------------- actions
    def check_in(self, visitor, flat_no):
        with self._lock:
            flat = self.registry.get(flat_no)
            if flat is None:
                raise ValueError(f"Flat {flat_no} does not exist.")
            if self._find_active_by_phone(visitor.phone):
                raise ValueError("This phone number is already marked IN. Mark them OUT first.")
            log = VisitLog(visitor, flat.number)
            self.logs.append(log)
            self._save()
        message = (f"🚪 {visitor.name} ({visitor.phone}) ENTERED {self.society}, Flat {flat.number} "
                   f"at {log.in_time.strftime('%I:%M %p')}. Purpose: {visitor.purpose}.")
        return log, self.notifications.notify(flat, "IN", message)

    def check_out(self, log_id):
        with self._lock:
            log = next((l for l in self.logs if l.id == log_id and l.status == "IN"), None)
            if log is None:
                raise ValueError("This visitor is not marked IN (maybe already checked out).")
            log.out_time = datetime.now()
            self._save()
            flat = self.registry.get(log.flat_no)
        message = (f"👋 {log.visitor.name} ({log.visitor.phone}) LEFT {self.society}, Flat {log.flat_no} "
                   f"at {log.out_time.strftime('%I:%M %p')}. Visit lasted {log.duration_text}.")
        return log, self.notifications.notify(flat, "OUT", message)

    def remove_flat(self, number):
        if any(l.flat_no == self.registry._key(number) for l in self.active()):
            raise ValueError("Cannot delete a flat while a visitor is still inside.")
        self.registry.remove(number)

    # ---------------------------------------------------------- queries
    def active(self):
        return [l for l in reversed(self.logs) if l.status == "IN"]

    def history(self):
        return list(reversed(self.logs))

    def stats(self):
        today = datetime.now().date()
        return {
            "inside": len(self.active()),
            "today": sum(1 for l in self.logs if l.in_time.date() == today),
            "exited": sum(1 for l in self.logs if l.out_time and l.out_time.date() == today),
            "alerts": self.notifications.count_today(),
        }

    # ---------------------------------------------------------- helpers
    def _find_active_by_phone(self, phone):
        return next((l for l in self.logs if l.visitor.phone == phone and l.status == "IN"), None)

    def _save(self):
        self.store.write([l.to_dict() for l in self.logs])
