"""
app.py - the web layer (Flask). Pages and forms only;
all real logic lives in models.py, manager.py and notifiers.py.
"""
import csv
import io
import os
from datetime import datetime

from flask import Flask, Response, flash, redirect, render_template, request, url_for

from config import DATA_DIR, Config
from manager import FlatRegistry, VisitorManager
from models import PURPOSES, TIME_FORMAT, Visitor
from notifiers import NotificationService, TelegramNotifier, TwilioSMSNotifier
from storage import JsonStore

app = Flask(__name__)
app.config.from_object(Config)

telegram = TelegramNotifier(Config.TELEGRAM_BOT_TOKEN)
sms = TwilioSMSNotifier(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN,
                        Config.TWILIO_FROM_NUMBER, Config.DEFAULT_COUNTRY_CODE)

service = NotificationService([telegram, sms], JsonStore(os.path.join(DATA_DIR, "notifications.json")))
registry = FlatRegistry(JsonStore(os.path.join(DATA_DIR, "flats.json")))
manager = VisitorManager(registry, service, JsonStore(os.path.join(DATA_DIR, "visits.json")),
                         Config.SOCIETY_NAME)


# ------------------------------------------------------------ template helpers
@app.template_filter("pretty")
def pretty(value, fmt="%d %b, %I:%M %p"):
    if isinstance(value, str):
        value = datetime.strptime(value, TIME_FORMAT)
    return value.strftime(fmt) if value else "—"


@app.template_filter("hue")
def hue(name):
    return sum(ord(c) for c in name) % 360


@app.template_filter("initials")
def initials(name):
    parts = name.replace(".", " ").split()
    return (parts[0][0] + (parts[-1][0] if len(parts) > 1 else "")).upper()


@app.context_processor
def inject_globals():
    return {"society": Config.SOCIETY_NAME, "channels": service.channel_status(), "purposes": PURPOSES}


def flash_delivery(prefix, record):
    """Tell the watchman exactly who got the alert."""
    results = record["results"]
    ok = [r["label"] for r in results if r["ok"]]
    bad = [f"{r['label']}: {r['detail']}" for r in results if not r["ok"]]
    if not results:
        flash(f"{prefix} Saved in the in-app inbox (no phone channel is set up yet).", "info")
    elif ok and not bad:
        flash(f"{prefix} Owner notified on {' & '.join(ok)}.", "success")
    elif ok:
        flash(f"{prefix} Owner notified on {' & '.join(ok)}. Not sent: {'; '.join(bad)}.", "warning")
    else:
        flash(f"{prefix} Alert could not be sent: {'; '.join(bad)}.", "warning")


# ------------------------------------------------------------------- pages
@app.get("/")
def index():
    return render_template("index.html", flats=registry.all(), active=manager.active(),
                           stats=manager.stats(), alerts=service.recent(limit=4))


@app.post("/checkin")
def check_in():
    try:
        visitor = Visitor(request.form.get("name"), request.form.get("phone"),
                          request.form.get("purpose", "Guest"))
        log, record = manager.check_in(visitor, request.form.get("flat_no", ""))
        flash_delivery(f"{visitor.name} marked IN for Flat {log.flat_no}.", record)
    except ValueError as e:
        flash(str(e), "error")
    return redirect(url_for("index"))


@app.post("/checkout/<log_id>")
def check_out(log_id):
    try:
        log, record = manager.check_out(log_id)
        flash_delivery(f"{log.visitor.name} marked OUT from Flat {log.flat_no}.", record)
    except ValueError as e:
        flash(str(e), "error")
    return redirect(url_for("index"))


@app.get("/history")
def history():
    return render_template("history.html", logs=manager.history(), flats=registry.all())


@app.get("/history.csv")
def history_csv():
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(["Visitor", "Phone", "Flat", "Purpose", "In time", "Out time", "Duration", "Status"])
    for l in manager.history():
        writer.writerow([l.visitor.name, l.visitor.phone, l.flat_no, l.visitor.purpose,
                         l.in_time.strftime(TIME_FORMAT),
                         l.out_time.strftime(TIME_FORMAT) if l.out_time else "", l.duration_text, l.status])
    return Response(buf.getvalue(), mimetype="text/csv",
                    headers={"Content-Disposition": "attachment; filename=visit_history.csv"})


@app.get("/notifications")
def notifications():
    flat_no = request.args.get("flat", "")
    return render_template("notifications.html", flats=registry.all(), selected=flat_no,
                           items=service.recent(flat_no or None, limit=100))


@app.get("/flats")
def flats():
    bot = None
    if telegram.enabled:
        try:
            bot = telegram.bot_username()
        except Exception:
            bot = None
    return render_template("flats.html", flats=registry.all(), bot=bot)


@app.post("/flats/add")
def flat_add():
    try:
        flat = registry.add(request.form.get("number"), request.form.get("owner_name"),
                            request.form.get("owner_phone"))
        flash(f"Flat {flat.number} added.", "success")
    except ValueError as e:
        flash(str(e), "error")
    return redirect(url_for("flats"))


@app.post("/flats/<number>/edit")
def flat_edit(number):
    try:
        registry.update(number, request.form.get("owner_name"), request.form.get("owner_phone"),
                        unlink_telegram=bool(request.form.get("unlink_telegram")))
        flash(f"Flat {number} updated.", "success")
    except ValueError as e:
        flash(str(e), "error")
    return redirect(url_for("flats"))


@app.post("/flats/<number>/delete")
def flat_delete(number):
    try:
        manager.remove_flat(number)
        flash(f"Flat {number} deleted.", "success")
    except ValueError as e:
        flash(str(e), "error")
    return redirect(url_for("flats"))


@app.post("/flats/<number>/test")
def flat_test(number):
    flat = registry.get(number)
    if flat is None:
        flash("Flat not found.", "error")
    else:
        record = service.notify(flat, "TEST", f"🔔 Test alert from {Config.SOCIETY_NAME}: "
                                f"alerts for Flat {flat.number} are working.")
        flash_delivery(f"Test alert for Flat {flat.number}.", record)
    return redirect(url_for("flats"))


@app.post("/telegram/sync")
def telegram_sync():
    if not telegram.enabled:
        flash("Telegram is not configured. Add TELEGRAM_BOT_TOKEN to your .env file.", "error")
        return redirect(url_for("flats"))
    try:
        requests_found = telegram.fetch_start_requests()
    except Exception as e:
        flash(f"Could not reach Telegram: {e}", "error")
        return redirect(url_for("flats"))
    linked = []
    for flat_no, chat_id, _name in requests_found:
        flat = registry.get(flat_no)
        if flat and flat.owner.telegram_chat_id != chat_id:
            registry.link_telegram(flat.number, chat_id)
            telegram.send_text(chat_id, f"✅ Linked! You will now get visitor alerts for "
                                        f"Flat {flat.number} of {Config.SOCIETY_NAME} here.")
            linked.append(flat.number)
    if linked:
        flash(f"Linked Telegram for Flat {', '.join(sorted(set(linked)))}.", "success")
    else:
        flash("No new links found. Ask owners to open their invite link and press Start, then sync again.", "info")
    return redirect(url_for("flats"))


if __name__ == "__main__":
    app.run(host=Config.HOST, port=Config.PORT, debug=True)
