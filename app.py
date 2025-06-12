from flask import Flask, render_template, redirect, abort
from datetime import datetime
import pytz
import os

app = Flask(__name__)

# Zona waktu WIB
JAKARTA_TZ = pytz.timezone('Asia/Jakarta')
LOGIN_START = JAKARTA_TZ.localize(datetime(2025, 6, 12, 19, 30))
LOGIN_END = JAKARTA_TZ.localize(datetime(2025, 6, 12, 21, 30))

# Gunakan environment variable agar aman
FORM_URL = os.getenv("FORM_URL", "https://forms.gle/epUL9ndhgoSf9oDp9")

@app.route("/")
def index():
    return render_template("index.html",
                           start_time=LOGIN_START.isoformat(),
                           end_time=LOGIN_END.isoformat())

@app.route("/secure-login")
def secure_login():
    now = datetime.now(JAKARTA_TZ)
    if LOGIN_START <= now < LOGIN_END:
        return redirect(FORM_URL)
    else:
        return abort(403, description="Login tidak tersedia saat ini.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

