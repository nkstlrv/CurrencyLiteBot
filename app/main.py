import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import time
from markups import MainMenuMarkup
from api import get_hryvna_rate
import logging

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)

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
    await message.answer(
        "Available currencies: (US Dollar, Euro, Hryvna)", parse_mode="HTML"
    )
    time.sleep(1)
    await message.answer(
        "<b>Main Menu</b> ⚙",
        parse_mode="HTML",
        reply_markup=MainMenuMarkup.markup,
    )


# Main Menu callback handler
@dp.callback_query_handler(text_startswith="m")
async def callback(call):
    # print(call.data)
    if call.data == "main_hryvna":
        rate: dict = get_hryvna_rate()

        if rate:
            usd_buy = rate.get("USD").get("buy")
            usd_sell = rate.get("USD").get("sale")

            eur_buy = rate.get("EUR").get("buy")
            eur_sell = rate.get("EUR").get("sale")

            message = (
                f"💲 <b>US Dollar (USD)</b>: \n"
                f"<b>Buy</b>:  {usd_buy} \n"
                f"<b>Sell</b>:  {usd_sell} \n\n"
                f"💶 <b>Euro (EUR)</b>: \n"
                f"<b>Buy</b>:  {eur_buy} \n"
                f"<b>Sell</b>:  {eur_sell}"
            )

            await bot.send_message(
                call.from_user.id, "<b><i>Hryvna USD/EUR Rate</i></b>: 🟨🟦"
            )
            await bot.send_message(call.from_user.id, message, parse_mode="html")
        else:
            await bot.send_message(call.from_user.id, "Currency server error")

    elif call.data == "main_calc":
        await bot.send_message(call.from_user.id, "Calculate Buy/Sell 💱")

    else:
        await bot.send_message(call.from_user.id, "Unknown command")


if __name__ == "__main__":
    logging.info("[STARTING SERVER...]")
    executor.start_polling(dp)
    logging.info("SERVER STOPPED]")
