import os
from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TP_TOKEN = os.getenv("TP_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

@app.route(f"/{TELEGRAM_TOKEN}", methods=["POST"])
def telegram_webhook():
    data = request.get_json()
    if "message" in data and "text" in data["message"]:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]
        if text.startswith("/flights"):
            search_flights(chat_id)
    return "ok", 200

def search_flights(chat_id):
    url = "https://api.travelpayouts.com/aviasales/v3/prices_for_dates"
    params = {
        "origin": "DEL",
        "destination": "BOM",
        "departure_at": "2025-08",
        "currency": "inr",
        "token": TP_TOKEN
    }
    response = requests.get(url, params=params)
    data = response.json()
    if "data" in data and len(data["data"]) > 0:
        flight = data["data"][0]
        msg = f"📍 {flight['origin']} → {flight['destination']}
💰 ₹{flight['value']}
📅 {flight['departure_at']}"
    else:
        msg = "No flights found."
    requests.post(f"{BASE_URL}/sendMessage", json={"chat_id": chat_id, "text": msg})

if __name__ == "__main__":
    app.run(debug=True, port=5000)