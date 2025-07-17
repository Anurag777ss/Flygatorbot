from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "7765244851:AAG25jPMQGeVwz4kdfhJxSbspuae4Sg-Y6w"
TP_API_TOKEN = "e9dff32d8528b74f272c6dfde795be68"
TP_API_URL = "https://api.travelpayouts.com/aviasales/v3/prices_for_dates"

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    message = data.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text", "")

    if text and chat_id:
        try:
            # Split user input: "DEL BOM 2025-08-01"
            parts = text.strip().split()
            if len(parts) == 3:
                origin, destination, date = parts
                params = {
                    "origin": origin.upper(),
                    "destination": destination.upper(),
                    "depart_date": date,
                    "one_way": "true",
                    "currency": "INR",
                    "token": TP_API_TOKEN
                }
                r = requests.get(TP_API_URL, params=params)
                data = r.json()

                if data.get("data"):
                    price = data["data"][0]["value"]
                    airline = data["data"][0]["airline"]
                    result = f"🛫 {origin} → {destination}\n📅 Date: {date}\n✈ Airline: {airline}\n💸 Price: ₹{price}"
                else:
                    result = "❌ No flights found for this route/date."
            else:
                result = "Please send in format:\n`DEL BOM 2025-08-01`"

            send_message(chat_id, result)

        except Exception as e:
            send_message(chat_id, "⚠️ Error: " + str(e))

    return "ok"
