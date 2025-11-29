# ------------------  IMPORTS  -------------------
from flask import Flask
from pyrogram import Client, filters

# ------------------  FLASK SERVER  -------------------
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running! 🚀"

# ------------------  TELEGRAM BOT  -------------------
API_ID = 38934704
API_HASH = "77bf14764bacdbf390aa0d1d786d97d7"
BOT_TOKEN = "8111461693:AAEwneZmqqvIaXTE_jp1-WZq4tK_DDxdus"

bot = Client(
    "A_BOT",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply("A Bot Online Hai 🔥")

# ------------------  RUN BOTH  -------------------
if __name__ == "__main__":
    bot.start()  # Telegram Bot Start
    app.run(host='0.0.0.0', port=10000)  # Flask Start (for Render)
