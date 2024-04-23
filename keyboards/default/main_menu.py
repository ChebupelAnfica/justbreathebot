from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Обо мне 🧘‍♀️"),
            KeyboardButton(text="О клубе и направлениях🌿")
        ],
        [
            KeyboardButton(text="Ответы на вопросы🧠"),
            KeyboardButton(text="Служба заботы 🫂")
        ],
        [
            KeyboardButton(text="Результаты")
        ]
    ],
    resize_keyboard=True
)
