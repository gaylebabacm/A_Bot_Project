import os
import asyncio
from flask import Flask
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# ---------- Flask Server ----------
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running properly! 🚀"

# ---------- Telegram Bot ----------
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    @dp.message(Command("start"))
    async def start_handler(message: types.Message):
        await message.answer("A Bot Online Hai 🔥 (Aiogram v3 READY!)")

    print("Polling started 🚀")
    await dp.start_polling(bot)

# ---------- START EVERYTHING ----------
if __name__ == "__main__":
    # Start Telegram Bot
    asyncio.run(main())
