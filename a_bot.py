# ------------------  IMPORTS  ------------------
from flask import Flask
from pyrogram import Client, filters
import os
import threading
import asyncio  # ADD THIS

# ------------------  FLASK SERVER  ------------------
app = Flask(__name__)

@app.route('/')
def home():
    return "A Bot Is Running 🚀"

# ------------------  TELEGRAM BOT  ------------------
API_ID = 38934704
API_HASH = "77bf14764bacdbf309aa0d1d786d97d7"
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Client(
    "A_BOT",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# ---- START COMMAND ----
@bot.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply("📨 Send Bot API Token")

# ---- BOT KO BACKGROUND THREAD ME RUN KARO ----
def start_bot():
    asyncio.run(bot.run())   # <-- Fix for ERROR

# ------------------  RUN BOTH ------------------
if __name__ == "__main__":
    threading.Thread(target=start_bot).start()  # Bot background me run hoga
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
