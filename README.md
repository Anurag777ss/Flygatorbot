# FlygatorBot (Webhook + Flask for Render - FREE)

This version of FlygatorBot uses **Flask + Webhook**, so it runs as a **Render Web Service (Free)** – no background worker required.

## 🚀 Features
- Telegram bot for flight search (via Travelpayouts API)
- City to IATA conversion (e.g., Delhi to Mumbai → DEL → BOM)
- Promo offer: 🎁 Book now & get a chance to win 100% cashback or a free trip!

---

## ☁️ Deploy on Render (FREE METHOD)

### 1. Upload Code to GitHub

```bash
git init
git add .
git commit -m "initial"
git remote add origin https://github.com/yourusername/flygatorbot.git
git push -u origin main
```

### 2. On Render

- Go to https://render.com
- Create New → **Web Service**
- Pick your GitHub repo

### 3. Render Settings

| Field              | Value                                  |
|-------------------|------------------------------------------|
| Build Command     | `pip install -r requirements.txt`        |
| Start Command     | `gunicorn app:app`                       |
| Instance Type     | Free                                     |

---

### 4. Add Environment Variables

| Key                    | Value                                                  |
|------------------------|--------------------------------------------------------|
| TELEGRAM_TOKEN         | your Telegram bot token                                |
| TRAVELPAYOUT_API_KEY   | your Travelpayout API token                            |
| WEBHOOK_URL            | your Render domain (e.g. `https://your-bot.onrender.com`) |

---

## 🔧 How It Works

- Flask app listens for Telegram updates via webhook.
- On startup, bot registers its webhook URL with Telegram.
- Free and fully functional on Render!