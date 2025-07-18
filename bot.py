import logging
import re
import requests
import json
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from config import TELEGRAM_TOKEN, TRAVELPAYOUT_API_KEY

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load IATA codes from file
def load_iata_codes():
    try:
        with open("iata_codes.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error("iata_codes.json not found!")
        raise Exception("iata_codes.json not found in project root.")

iata_dict = load_iata_codes()

def find_iata(city_name):
    for code, city in iata_dict.items():
        if city_name.lower() in city.lower():
            return code
    return None

def parse_route(text):
    match = re.search(r"(.+) to (.+)", text, re.IGNORECASE)
    if match:
        from_city = match.group(1).strip()
        to_city = match.group(2).strip()
        from_code = find_iata(from_city)
        to_code = find_iata(to_city)
        if from_code and to_code:
            return from_code, to_code
    return None, None

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('👋 Welcome to FlygatorBot! Send me a route like "Delhi to Mumbai".')

def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    from_code, to_code = parse_route(text)
    if from_code and to_code:
        update.message.reply_text(f"Searching flights from {from_code} → {to_code}...\n🎁 Book now & get a chance to win 100% cashback or a free trip!")
        result = search_flights(from_code, to_code)
        update.message.reply_text(result)
    else:
        update.message.reply_text("Please enter a route like: CityA to CityB")

def search_flights(origin, destination):
    url = "https://api.travelpayouts.com/v2/prices/latest"
    params = {
        "origin": origin,
        "destination": destination,
        "currency": "usd",
        "token": TRAVELPAYOUT_API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    if "data" in data and data["data"]:
        flight = data["data"][0]
        return f"✈️ {origin} → {destination}\nPrice: ${flight['price']}\nAirline: {flight['airline']}"
    else:
        return "No flights found at the moment."

def main():
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()