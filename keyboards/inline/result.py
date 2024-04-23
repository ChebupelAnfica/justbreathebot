from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

connection = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Присоединиться", callback_data="connection")
        ]
    ]
)