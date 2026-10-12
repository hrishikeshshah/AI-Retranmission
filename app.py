import os
from pathlib import Path
from flask import Flask, send_from_directory

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__, static_folder=None)

@app.get("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")

@app.get("/<path:filename>")
def public_files(filename):
    # Allows local CSS, JavaScript, images, or other files if added later.
    return send_from_directory(BASE_DIR, filename)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
