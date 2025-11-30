# ------------------ IMPORTS ------------------
from flask import Flask
from pyrogram import Client, filters, idle
import os
import asyncio

# ------------------ FLASK SERVER ------------------
app = Flask(__name__)

@app.route('/')
def home():
    return "A Bot Is Running 🚀"

# ------------------ TELEGRAM BOT ------------------
API_ID = 38934704
API_HASH = "77bf14764bacdbf309aa0d1d786d97d7"
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Client(
    "A_BOT",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ----------- START COMMAND -----------
@bot.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply("📨 Send Bot API Token")

# ----------- BOT RUN FUNCTION -----------
async def main():
    await bot.start()
    print("Telegram Bot Started Successfully ✔️")
    await idle()     # <-- IMPORTANT FIX!

# ------------------ RUN BOTH ------------------
if __name__ == "__main__":
    # Flask ko background me chalao
    from threading import Thread
    Thread(target=lambda: app.run(host="0.0.0.0", port=int(os.getenv("PORT", 10000)))).start()

    # Async Telegram Bot
    asyncio.run(main())
