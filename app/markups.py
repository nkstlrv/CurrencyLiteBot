from aiogram import types


class MainMenuMarkup:
    b1 = types.InlineKeyboardButton(
        "Hryvna Exchange Rate", callback_data="main_fresh_currencies"
    )
    b2 = types.InlineKeyboardButton(
        "Get Fresh Rate 📊", callback_data="main_fresh_currencies"
    )
    b3 = types.InlineKeyboardButton(
        "Calculate Buy/Sell 🤝", callback_data="main_fresh_currencies"
    )
    markup = types.InlineKeyboardMarkup(row_width=1).add(b1, b2, b3)
