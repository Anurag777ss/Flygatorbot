# FlygatorBot (Render Deployment Ready)

FlygatorBot is a Telegram bot that helps users search for flights using the Travelpayouts API.

## ✈️ Features
- Flight search using Travelpayouts API
- Auto conversion of city names to IATA codes (e.g., "Delhi to Mumbai" → "DEL → BOM")
- Promotional offer: 🎁 Book now & get a chance to win 100% cashback or a free trip!

## 🚀 How to Use
1. Start the bot on Telegram: [@flygatorbot](https://t.me/flygatorbot)
2. Send a message like "Delhi to Mumbai" or "New York to London"
3. Receive flight offers and promotional details

## ☁️ Deploying on Render

### 1. Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/flygatorbot.git
git push -u origin main
```

### 2. Create a New Web Service on Render
- Build Command: `pip install -r requirements.txt`
- Start Command: `python bot.py`
- Instance Type: Free

### 3. Set Environment Variables
In the Render Dashboard → Environment tab, add:

```
TELEGRAM_TOKEN = 7765244851:AAG25jPMQGeVwz4kdfhJxSbspuae4Sg-Y6w
TRAVELPAYOUT_API_KEY = e9dff32d8528b74f272c6dfde795be68
```

### 4. Done! 🎉