# VisitorEntrySystem

A digital replacement for the watchman's paper visitor register.
Python OOP + Flask. The visitor's name, phone and flat are recorded, and the
flat owner gets a real alert on their phone when the visitor enters and leaves.

## Run it
    pip install -r requirements.txt
    python app.py
Open http://127.0.0.1:5000

The app works immediately with sample flats. Alerts are always saved in the
in-app inbox (Alerts page). To also get alerts on a phone, set up Telegram
and/or SMS below.

## Telegram alerts (free, recommended)
1. In Telegram, message **@BotFather**, send `/newbot`, copy the token.
2. Copy `.env.example` to `.env` and paste the token as `TELEGRAM_BOT_TOKEN`.
3. Restart the app and open **Flats**.
4. Press **Invite link** for a flat and send it to that owner.
5. The owner opens the link and presses **Start** in Telegram.
6. Press **Sync Telegram links** in the app. Use **Test** to check it works.

## SMS alerts (Twilio)
Put `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_FROM_NUMBER` in `.env`.
Notes: trial accounts only send to verified numbers; Indian numbers also need
DLT registration for dependable delivery, so SMS may be filtered even when the
code is correct. Delivery failures are shown on the Alerts page.

## Project structure
    app.py          Flask routes (web layer only)
    manager.py      FlatRegistry + VisitorManager (check-in / check-out rules, stats)
    notifiers.py    Notifier (abstract), TelegramNotifier, TwilioSMSNotifier, NotificationService
    models.py       Person, Visitor, Resident, Flat, VisitLog
    storage.py      JsonStore (thread-safe JSON files in data/)
    config.py       settings from .env
    templates/ static/   HTML, CSS, JS

## OOP concepts (for your viva / report)
- Encapsulation: Person validates name and 10-digit phone through property setters.
- Inheritance: Visitor and Resident extend Person.
- Abstraction: Notifier is an abstract base class with abstract `send()`.
- Polymorphism: NotificationService calls `send()` on every channel without
  knowing if it is Telegram or SMS. Add Email/WhatsApp by writing one new subclass.
- Composition: Flat has a Resident; VisitLog has a Visitor; VisitorManager has a
  FlatRegistry and NotificationService.

## Data
Stored as JSON in the `data/` folder (created automatically):
flats.json, visits.json, notifications.json. Delete a file to reset it.
