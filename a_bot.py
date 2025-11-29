# ---------------- IMPORTS ----------------
from flask import Flask
from pyrogram import Client, filters
import os

# ---------------- FLASK SERVER ----------------
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running! 🚀"


# ---------------- TELEGRAM BOT ----------------
API_ID = 38934704
API_HASH = "77b7f14764bacdbf390aa0d1786d97d7"
BOT_TOKEN = "8111461693:AAEwneZmqqylaXT0_jp1-Wz4qtK_DDxuds"

bot = Client(
    "A_BOT",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply("A Bot Online Hai 🔥")


# ---------------- RUN BOTH ----------------
if __name__ == "__main__":
    bot.start()  # Telegram bot start
    
    # Flask for Render – port lena जरूरी
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
