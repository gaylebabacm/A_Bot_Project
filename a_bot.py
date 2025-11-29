from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from flask import Flask
import os

# ---------------- FLASK SERVER ----------------
app = Flask(name)

@app.route("/")
def home():
    return "Bot is running! 🚀"

# ---------------- TELEGRAM BOT ----------------
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Environment se le raha
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.answer("A Bot Online Hai 🔥")

# ---------------- RUNNING ----------------
if name == "main":
    # Telegram Bot Start
    from threading import Thread
    def start_bot():
        executor.start_polling(dp, skip_updates=True)

    Thread(target=start_bot).start()

    # Flask Server Render ke liye
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
