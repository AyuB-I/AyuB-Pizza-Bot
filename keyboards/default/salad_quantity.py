from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


salad_quantity = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1"),
            KeyboardButton(text="2"),
            KeyboardButton(text="3")
        ],
        [
            KeyboardButton(text="4"),
            KeyboardButton(text="5"),
            KeyboardButton(text="6")
        ],
        [
            KeyboardButton(text="7"),
            KeyboardButton(text="8"),
            KeyboardButton(text="9")
        ],
        [
            KeyboardButton(text="Назад\U00002B05"),
            KeyboardButton(text="Главная\U00002B06")
        ]
    ],
    resize_keyboard=True
)
