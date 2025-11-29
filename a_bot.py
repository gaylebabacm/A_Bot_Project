import asyncio
from flask import Flask
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command  # <-- IMPORTANT CHANGE
import os

# --------- FLASK SERVER ---------
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running with Aiogram v3! 🚀"

# --------- TELEGRAM BOT CONFIG ---------
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# --------- COMMAND HANDLER (FIXED) ---------
@dp.message(Command("start"))  # <-- CORRECT FOR Aiogram v3
async def start_handler(message: types.Message):
    await message.answer("A Bot Online Hai 🔥 (Aiogram v3)")

# --------- RUN BOTH ---------
async def run_bot():
    await dp.start_polling(bot)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(run_bot())

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
