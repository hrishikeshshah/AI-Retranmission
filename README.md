# AI Smart Retransmission Simulator — Render Web Service

This version runs as a Python web service (Flask + Gunicorn), not a Render Static Site. The simulator itself remains in `index.html` and runs in the visitor's browser.

## Deploy from GitHub

1. Upload `app.py`, `index.html`, `requirements.txt`, `render.yaml`, and this README to the **root** of your GitHub repository.
2. In Render, select **New + → Web Service** (not Static Site) and connect the repository.
3. Set **Runtime** to Python.
4. Set **Build Command** to `pip install -r requirements.txt`.
5. Set **Start Command** to `gunicorn app:app --bind 0.0.0.0:$PORT`.
6. Create the Web Service and open its `onrender.com` URL after deployment finishes.

If Render automatically reads `render.yaml`, it can use the configuration in that file. Do not use `streamlit run app.py` for this Flask deployment.

## Run locally (optional)

```bash
python -m pip install -r requirements.txt
python app.py
```
Then open `http://127.0.0.1:5000`.
