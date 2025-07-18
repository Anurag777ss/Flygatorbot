import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TRAVELPAYOUT_API_KEY = os.getenv("TRAVELPAYOUT_API_KEY")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

if not TELEGRAM_TOKEN or not TRAVELPAYOUT_API_KEY or not WEBHOOK_URL:
    raise Exception("Missing required environment variables.")