from pyrogram import Client, filters

API_ID = 38934704
API_HASH = "77bf14764bacdbf309aa0d1d786d97d7"
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

bot = Client(
    "A_BOT",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply("A Bot Online Hai 🔥")

if __name__ == "__main__":
    bot.run()
