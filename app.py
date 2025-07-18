import json
import re
import requests
from flask import Flask, request
from config import TELEGRAM_TOKEN, TRAVELPAYOUT_API_KEY, WEBHOOK_URL

app = Flask(__name__)

# Load IATA data
def load_iata():
    with open("iata_codes.json") as f:
        return json.load(f)

iata_dict = load_iata()

def find_iata(city):
    for code, name in iata_dict.items():
        if city.lower() in name.lower():
            return code
    return None

def parse_route(text):
    match = re.search(r"(.+) to (.+)", text, re.IGNORECASE)
    if match:
        return find_iata(match.group(1)), find_iata(match.group(2))
    return None, None

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data and "text" in data["message"]:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]
        from_code, to_code = parse_route(text)
        if from_code and to_code:
            msg = f"Searching flights from {from_code} → {to_code}...\n🎁 Book now & get a chance to win 100% cashback or a free trip!"
            send_message(chat_id, msg)
            send_message(chat_id, search_flights(from_code, to_code))
        else:
            send_message(chat_id, "Please enter route like: CityA to CityB")
    return "OK", 200

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
        f = data["data"][0]
        return f"✈️ {origin} → {destination}\nPrice: ${f['price']}\nAirline: {f['airline']}"
    return "No flights found."

def set_webhook():
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/setWebhook"
    webhook_url = f"{WEBHOOK_URL}"
    requests.get(url, params={"url": webhook_url})

# Register webhook on startup
set_webhook()