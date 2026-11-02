"""
models.py - the data classes.

  Encapsulation : name / phone validation inside Person (property setters)
  Inheritance   : Visitor and Resident extend Person
  Composition   : a Flat HAS a Resident (its owner); a VisitLog HAS a Visitor
"""
import re
import uuid
from datetime import datetime

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
PURPOSES = ["Guest", "Delivery", "Service / Repair", "Cab / Taxi", "Other"]
FLAT_PATTERN = re.compile(r"[A-Za-z0-9_-]{1,10}")


class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone  # goes through the setter below

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        value = (value or "").strip()
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        value = (value or "").strip()
        if not re.fullmatch(r"\d{10}", value):
            raise ValueError("Phone number must be exactly 10 digits.")
        self._phone = value


class Visitor(Person):
    """An unknown person entering the residency."""

    def __init__(self, name, phone, purpose="Guest"):
        super().__init__(name, phone)
        self.purpose = purpose if purpose in PURPOSES else "Other"


class Resident(Person):
    """A flat owner. Receives the notifications."""

    def __init__(self, name, phone, telegram_chat_id=None):
        super().__init__(name, phone)
        self.telegram_chat_id = telegram_chat_id

    @property
    def telegram_linked(self):
        return bool(self.telegram_chat_id)


class Flat:
    def __init__(self, number, owner):
        number = (number or "").strip().upper()
        if not FLAT_PATTERN.fullmatch(number):
            raise ValueError("Flat number may use letters, digits, - and _ (max 10 characters).")
        self.number = number
        self.owner = owner

    def to_dict(self):
        return {
            "number": self.number,
            "owner_name": self.owner.name,
            "owner_phone": self.owner.phone,
            "telegram_chat_id": self.owner.telegram_chat_id,
        }

    @classmethod
    def from_dict(cls, d):
        return cls(d["number"], Resident(d["owner_name"], d["owner_phone"], d.get("telegram_chat_id")))


class VisitLog:
    """One row of the register: who, where, when in, when out."""

    def __init__(self, visitor, flat_no, in_time=None, out_time=None, log_id=None):
        self.id = log_id or uuid.uuid4().hex[:8]
        self.visitor = visitor
        self.flat_no = flat_no
        self.in_time = in_time or datetime.now()
        self.out_time = out_time

    @property
    def status(self):
        return "IN" if self.out_time is None else "OUT"

    @property
    def duration_text(self):
        end = self.out_time or datetime.now()
        minutes = int((end - self.in_time).total_seconds() // 60)
        if minutes < 1:
            return "under 1 min"
        hours, mins = divmod(minutes, 60)
        return f"{hours}h {mins:02d}m" if hours else f"{mins} min"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.visitor.name,
            "phone": self.visitor.phone,
            "purpose": self.visitor.purpose,
            "flat_no": self.flat_no,
            "in_time": self.in_time.strftime(TIME_FORMAT),
            "out_time": self.out_time.strftime(TIME_FORMAT) if self.out_time else None,
        }

    @classmethod
    def from_dict(cls, d):
        out = datetime.strptime(d["out_time"], TIME_FORMAT) if d.get("out_time") else None
        return cls(
            Visitor(d["name"], d["phone"], d.get("purpose", "Guest")),
            d["flat_no"],
            datetime.strptime(d["in_time"], TIME_FORMAT),
            out,
            d.get("id"),
        )
