# ------------------ IMPORTS ------------------
from flask import Flask
from pyrogram import Client, filters
import os

# ------------------ FLASK SERVER ------------------
app = Flask(__name__)

@app.route('/')
def home():
    return "A Bot is Running 🚀"

# ------------------ TELEGRAM BOT ------------------
API_ID = 38934704
API_HASH = "77bf14764bacdbf309aa0d1d786d97d7"
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Environment Variable se token le raha hai

bot = Client("A_BOT", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ----- START COMMAND -----
@bot.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply("📩 Send Bot API Token")

# ------------------ RUN BOTH ------------------
if __name__ == "__main__":
    bot.start()
    port = int(os.environ.get("PORT", 5000))  # PORT Render automatic set karega
    app.run(host='0.0.0.0', port=port)
