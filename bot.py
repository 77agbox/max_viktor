import os
from maxbot import MaxBot
from maxbot.types import Message

bot = MaxBot(token=os.getenv("BOT_TOKEN"))

@bot.message_handler()
async def handle_message(message: Message):
    text = message.text.lower()

    if text == "привет":
        await message.answer("Привет! 👋 Я бот центра Виктория")
    elif text == "кружки":
        await message.answer("У нас есть: танцы, рисование, программирование")
    else:
        await message.answer("Напиши: привет или кружки")

bot.run()
