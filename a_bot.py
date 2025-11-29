import asyncio
from flask import Flask
from aiogram import Bot, Dispatcher, types
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

# --------- COMMAND HANDLER ---------
@dp.message(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("A Bot Online Hai 🔥 (Aiogram v3)")

# --------- RUN BOTH ---------
async def run_bot():
    await dp.start_polling(bot)

if __name__ == "__main__":
    # Telegram Bot BACKGROUND me chalana
    loop = asyncio.get_event_loop()
    loop.create_task(run_bot())

    # Flask server RUN render ke liye
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
