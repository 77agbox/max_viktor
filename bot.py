import os
from maxbot import Bot, Message

bot = Bot(token=os.getenv("BOT_TOKEN"))

@bot.on_message()
async def handle_message(msg: Message):
    text = msg.text.lower()

    if text == "привет":
        await msg.reply("Привет! 👋 Я бот центра Виктория")
    elif text == "кружки":
        await msg.reply("У нас есть: танцы, рисование, программирование")
    else:
        await msg.reply("Напиши: привет или кружки")

bot.run()
