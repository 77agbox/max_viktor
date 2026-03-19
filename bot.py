import os
from flask import Flask, request, jsonify
import requests

TOKEN = os.getenv("BOT_TOKEN")
URL = f"https://botapi.max.ru/messages"
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

app = Flask(__name__)

@app.route("/", methods=["POST"])
def handle_update():
    try:
        data = request.json
        print(data)
        
        # Получаем чат ID и текст сообщения
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '').strip().lower()
    
        # Проверяем состояние и выполняем соответствующую реакцию
        if text == 'привет':
            send_message(chat_id, "Привет! 👋 Я бот центра Виктория.")
        elif text == 'кружки':
            send_message(chat_id, "У нас есть: танцы, рисование, программирование.")
        else:
            send_message(chat_id, "Напишите: привет или кружки.")
            
        return jsonify({"ok": True}), 200
    except Exception as e:
        print(e)
        return jsonify({"ok": False}), 500

def set_webhook():
    response = requests.post(
        f"{URL}/setWebhook",
        json={"webhook_url": WEBHOOK_URL},
        headers={'Authorization': f'Bearer {TOKEN}'}
    )
    print(response.text)

def send_message(chat_id, text):
    response = requests.post(
        f"{URL}/sendMessage",
        json={"chat_id": chat_id, "text": text},
        headers={'Authorization': f'Bearer {TOKEN}'}
    )
    print(response.text)

if __name__ == "__main__":
    set_webhook()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
