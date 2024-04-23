from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

pay = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1 месяц 130BYN/40$", callback_data="level1")
        ],
        [
            InlineKeyboardButton(text="3 месяца 275 BYN/85$", callback_data="level2")
        ],
        [
            InlineKeyboardButton(text="6 месяцев 535 BYN/165$", callback_data="level3")
        ],
        [
            InlineKeyboardButton(text="Закрыть", callback_data="cancel")
        ]
    ]
)

pay_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Оплатить", url="https://ya.ru/")
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data="connection")
        ]
    ]
)
