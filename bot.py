import os
import requests
import time

TOKEN = os.getenv("BOT_TOKEN")
URL = f"https://botapi.max.ru/messages"

def get_updates():
    response = requests.get(f"{URL}/getUpdates", params={"access_token": TOKEN})
    return response.json()

def send_message(chat_id, text):
    requests.post(f"{URL}/send", json={
        "chat_id": chat_id,
        "text": text,
        "access_token": TOKEN
    })

def main():
    offset = 0

    while True:
        data = get_updates()

        if "result" in data:
            for update in data["result"]:
                message = update.get("message")
                if not message:
                    continue

                chat_id = message["chat"]["id"]
                text = message.get("text", "").lower()

                if text == "привет":
                    send_message(chat_id, "Привет! 👋 Я бот центра Виктория")
                elif text == "кружки":
                    send_message(chat_id, "У нас есть: танцы, рисование, программирование")
                else:
                    send_message(chat_id, "Напиши: привет или кружки")

        time.sleep(2)

if __name__ == "__main__":
    main()
