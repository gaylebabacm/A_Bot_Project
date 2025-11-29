import asyncio
from flask import Flask
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import os

# --------- FLASK APP ---------
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running with Aiogram v3! 🚀"

# --------- TELEGRAM BOT CONFIG ---------
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# START COMMAND
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("A Bot Online Hai 🔥 (Aiogram v3 Running!)")

# --------- RUN BOT ---------
async def start_bot():
    await dp.start_polling(bot)

if __name__ == "__main__":
    # Python 3.13 fix (new event loop)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(start_bot())  # <-- IMPORTANT FIX!

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
