from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

questions = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Какой уровень?", callback_data="questions1")
        ],
        [
            InlineKeyboardButton(text="Сколько стоит?", callback_data="questions2")
        ],
        [
            InlineKeyboardButton(text="Что мне нужно для тренировок?", callback_data="questions3")
        ],
        [
            InlineKeyboardButton(text="Как ориентироваться в канале?", callback_data="questions4")
        ],
        [
            InlineKeyboardButton(text="Что за тренировка в прямом эфире?", callback_data="questions5")
        ],
        [
            InlineKeyboardButton(text="Закрыть", callback_data="cancel")
        ]
    ],
)

back_to_questions = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад к вопросам", callback_data="back_to_all_questions")
        ]
    ]
)

connection = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Присоединиться", callback_data="connection")
        ]
    ]
)

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

