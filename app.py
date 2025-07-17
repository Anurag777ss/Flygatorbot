
from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = "YOUR_TELEGRAM_TOKEN"
TRAVELPAYOUT_TOKEN = "YOUR_TRAVELPAYOUT_TOKEN"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text.startswith("/start"):
            send_message(chat_id, "Welcome to FlyGatorBot! ✈️ Send me a city or airport name to search flights.")

        else:
            reply = search_flights(text)
            send_message(chat_id, reply)

    return "ok", 200

def send_message(chat_id, text):
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

def search_flights(query):
    url = f"https://api.travelpayouts.com/aviasales/v3/prices_for_dates"
    params = {
        "origin": query[:3].upper(),
        "destination": "DEL",
        "depart_date": "2025-08-01",
        "return_date": "2025-08-10",
        "token": TRAVELPAYOUT_TOKEN
    }
    res = requests.get(url, params=params)
    if res.status_code == 200:
        data = res.json().get("data", [])
        if not data:
            return "No flights found. Try another airport or city."
        flights = [f"{d['value']} INR - {d['depart_date']} to {d['return_date']}" for d in data[:3]]
        return "\n".join(flights)
    else:
        return "Flight search failed. Try again later."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
