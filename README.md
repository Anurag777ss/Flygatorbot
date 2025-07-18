# FlygatorBot

FlygatorBot is a Telegram bot that helps users search for flights using the Travelpayouts API.

## ✈️ Features
- Flight search using Travelpayouts API
- Auto conversion of city names to IATA codes (e.g., "Delhi to Mumbai" → "DEL → BOM")
- Promotional offer: 🎁 Book now & get a chance to win 100% cashback or a free trip!

## 🚀 How to Use
1. Start the bot on Telegram: [@flygatorbot](https://t.me/flygatorbot)
2. Send a message like "Delhi to Mumbai" or "New York to London"
3. Receive flight offers and promotional details

## 🔧 Setup Instructions

### 1. Clone & Configure
```bash
git clone https://github.com/yourusername/flygatorbot.git
cd flygatorbot
```
Add your credentials in `config.py`.

### 2. Deploy
- You can use platforms like [Railway](https://railway.app), [Render](https://render.com), or [Heroku](https://heroku.com).
- Or deploy on your own server using Python 3.10+.

### 3. Run Bot
```bash
pip install -r requirements.txt
python bot.py
```

## 🧾 Environment Variables (in config.py)
- TELEGRAM_TOKEN = 'Your Telegram Bot Token'
- TRAVELPAYOUT_API_KEY = 'Your Travelpayout API Token'