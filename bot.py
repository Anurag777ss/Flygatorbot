import os
import requests
from flask import Flask, request

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("7765244851:AAG25jPMQGeVwz4kdfhJxSbspuae4Sg-Y6w")
TRAVELPAYOUTS_TOKEN = os.getenv("e9dff32d8528b74f272c6dfde795be68")

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)

def get_cheapest_flight():
    url = "https://api.travelpayouts.com/v2/prices/latest"
    headers = {"X-Access-Token": TRAVELPAYOUTS_TOKEN}
    params = {"origin": "DEL", "destination": "BOM", "currency": "INR"}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    if data.get("data"):
        price = data["data"][0]["price"]
        return f"Cheapest flight from Delhi to Mumbai: ₹{price}"
    return "No flight data available."

@app.route(f"/{TELEGRAM_TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "").lower()
        if "flight" in text:
            reply = get_cheapest_flight()
        else:
            reply = "Type 'flight' to get cheapest flight info from Delhi to Mumbai."
        send_message(chat_id, reply)
    return {"ok": True}

@app.route("/", methods=["GET"])
def home():
    return "Bot is running!"

if __name__ == "__main__":
    app.run()
