from aiogram import Bot, Dispatcher, types
import asyncio
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def start_handler(message: types.Message):
    if message.text == "/start":
        await message.reply("📩 Send Bot API Token")

async def main():
    print("Telegram Bot Started Successfully ✔️")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
