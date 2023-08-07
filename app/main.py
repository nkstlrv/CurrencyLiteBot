import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import time
from markups import MainMenuMarkup

# loading local environment variables
load_dotenv()

TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
bot = Bot(token=TELEGRAM_API_KEY)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        f"Hello there, <i><b>{message.chat.first_name}</b></i> 👋",
        parse_mode="HTML",
        reply_markup=types.ReplyKeyboardRemove(),
    )
    time.sleep(1)
    await message.answer("This is <b>CurrencyLite</b> bot 🤖", parse_mode="HTML")
    time.sleep(1)
    await message.answer(
        "<b>Main Menu</b> ⚙",
        parse_mode="HTML",
        reply_markup=MainMenuMarkup.markup,
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
