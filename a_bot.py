from flask import Flask
from pyrogram import Client, filters
import os

# Flask Server
app = Flask(__name__)

@app.route('/')
def home():
    return "Worker Running Successfully! 🔥"

# Telegram Bot Credentials from Environment Variables
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Telegram Bot Client
bot = Client(
    "A_BOT",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# START Command
@bot.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply("[ Send bot api token ]")

# Run Both
if __name__ == "__main__":
    bot.start()
    print("Telegram Bot Started Successfully ✔️")
    app.run(host='0.0.0.0', port=10000)
