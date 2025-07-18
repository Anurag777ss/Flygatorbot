import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TRAVELPAYOUT_API_KEY = os.getenv("TRAVELPAYOUT_API_KEY")

if not TELEGRAM_TOKEN or not TRAVELPAYOUT_API_KEY:
    raise Exception("⚠️ TELEGRAM_TOKEN or TRAVELPAYOUT_API_KEY is missing in environment variables!")