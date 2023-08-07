from aiogram import types


class MainMenuMarkup:
    b1 = types.InlineKeyboardButton(
        "Hryvna USD/EUR Rate 🟨🟦", callback_data="main_hryvna"
    )
    b2 = types.InlineKeyboardButton("Calculate Buy/Sell 💱", callback_data="main_calc")
    markup = types.InlineKeyboardMarkup(row_width=1).add(b1, b2)
