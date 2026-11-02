"""storage.py - a small thread-safe JSON file store."""
import json
import os
import threading


class JsonStore:
    def __init__(self, path):
        self.path = path
        self._lock = threading.RLock()
        os.makedirs(os.path.dirname(path), exist_ok=True)

    def read(self):
        with self._lock:
            if not os.path.exists(self.path):
                return []
            try:
                with open(self.path, encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, OSError):
                return []

    def write(self, data):
        with self._lock:
            tmp = self.path + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            os.replace(tmp, self.path)  # atomic: never leaves a half-written file
