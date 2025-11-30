# ------------------ IMPORTS ------------------
from flask import Flask
from pyrogram import Client, filters, idle
import os
import asyncio
from threading import Thread

# ------------------ FLASK SERVER ------------------
app = Flask(__name__)

@app.route("/")
def home():
    return "A Bot is Running 🚀"

# ------------------ TELEGRAM BOT SETUP ------------------
API_ID = 38934704
API_HASH = "77bf14764bacdbf309aa0d1d786d97d7"
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Render env se lega

bot = Client(
    "A_BOT",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply("📨 Send Bot API Token")

# ------------------ BOT START FUNCTION ------------------
async def run_bot():
    await bot.start()
    print("Bot Started ✔️")
    await idle()

def start_flask():
    port = int(os.getenv("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# ------------------ RUN ------------------
if __name__ == "__main__":
    # Flask alag thread me
    Thread(target=start_flask).start()

    # Bot main thread me
    asyncio.run(run_bot())
