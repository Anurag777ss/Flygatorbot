from flask import Flask, request
import requests
from config import TELEGRAM_TOKEN, TP_TOKEN

app = Flask(__name__)

@app.route('/')
def home():
    return "FlyGatorBot is running!"

@app.route(f'/{TELEGRAM_TOKEN}', methods=['POST'])
def telegram_webhook():
    data = request.json
    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")

    if text.startswith("/start"):
        send_message(chat_id, "Welcome to FlyGator Bot ✈️
Send your flight query like:
Delhi to Mumbai on 2024-08-01")
    elif "to" in text.lower():
        reply = get_flight_data(text)
        send_message(chat_id, reply)
    else:
        send_message(chat_id, "❗Invalid format.
Try: Delhi to Mumbai on 2024-08-01")

    return "ok"

def get_flight_data(query):
    try:
        parts = query.lower().split(" on ")
        route = parts[0].strip().split(" to ")
        date = parts[1].strip()
        origin = route[0].strip().lower()
        dest = route[1].strip().lower()

        url = f"https://api.travelpayouts.com/v2/prices/latest"
        params = {
            "origin": origin[:3].upper(),
            "destination": dest[:3].upper(),
            "depart_date": date,
            "currency": "INR",
            "token": TP_TOKEN
        }
        res = requests.get(url, params=params).json()

        if res.get("data"):
            ticket = res["data"][0]
            price = ticket["price"]
            airline = ticket["airline"]
            flight_date = ticket["departure_at"]
            return f"🎫 {origin.upper()} to {dest.upper()}
Airline: {airline}
Date: {flight_date}
Price: ₹{price}"
        else:
            return "No flights found for that route/date."

    except Exception as e:
        return "Something went wrong. Please try again."

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(debug=True)
