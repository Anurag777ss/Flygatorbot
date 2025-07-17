
# FlyGatorBot

Telegram bot to search flights using Travelpayout API.

## Setup

1. Replace `YOUR_TELEGRAM_TOKEN` and `YOUR_TRAVELPAYOUT_TOKEN` in `app.py`
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run locally:
```
python app.py
```
4. Deploy on Render, Replit, or Railway and set Telegram webhook to:
```
https://your-app-url/webhook
```

## Hosting (Render)
- Create new web service on [https://render.com/](https://render.com/)
- Add your repo
- Use build command: `pip install -r requirements.txt`
- Use start command: `python app.py`
