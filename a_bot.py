# ------------------ IMPORTS ------------------
from flask import Flask
from pyrogram import Client, filters
from pyrogram.types import Message
import os
import threading

# ------------------ FLASK SERVER (Render ke liye) ------------------
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Bot is running! 🚀"


# ------------------ TELEGRAM BOT CONFIG ------------------
API_ID = 38934704
API_HASH = "77bf14764bacdbf309aa0d1d786d97d7"
BOT_TOKEN = "8111461693:AAFWnshHaD-2IcujwaTyA-XNMdujvbsMxZQ"

# sirf ye ID wala banda admin hai
ADMIN_ID = 7266466699


# ------------------ PYROGRAM CLIENT ------------------
bot = Client(
    "A_BOT",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


# ------------------ ADMIN FILTER ------------------
def is_admin(_, __, message: Message):
    return message.from_user and message.from_user.id == ADMIN_ID

admin_filter = filters.create(is_admin)


# ------------------ HANDLERS ------------------

# normal /start – sabke liye
@bot.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply("A Bot Online Hai 🔥")


# sirf admin ke liye – check bot alive
@bot.on_message(filters.command("ping") & admin_filter)
async def ping_handler(client, message):
    await message.reply("Boss, bot alive 😎")


# sirf admin – bot ka bio (about) change
@bot.on_message(filters.command("setbio") & admin_filter)
async def set_bio_handler(client, message):
    parts = message.text.split(" ", 1)
    if len(parts) == 1:
        return await message.reply("Usage: /setbio naya bio")
    new_bio = parts[1]
    await client.set_bot_info(about=new_bio)
    await message.reply("Bio updated 🔐")


# sirf admin – bot ka description change
@bot.on_message(filters.command("setdesc") & admin_filter)
async def set_desc_handler(client, message):
    parts = message.text.split(" ", 1)
    if len(parts) == 1:
        return await message.reply("Usage: /setdesc naya description")
    new_desc = parts[1]
    await client.set_bot_info(description=new_desc)
    await message.reply("Description updated 🔐")


# ------------------ RUN BOT + FLASK SAATH ME ------------------
def run_bot():
    bot.run()   # Telegram bot yaha continuously chalega


if __name__ == "__main__":
    # bot ko background thread me chalao
    threading.Thread(target=run_bot, daemon=True).start()

    # Render ke liye HTTP port open karo
    port = int(os.environ.get("PORT", 5000))
    flask_app.run(host="0.0.0.0", port=port)
