from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Пицца\U0001f355")
        ],
        [
            KeyboardButton(text="Салаты\U0001F957"),
            KeyboardButton(text="Напитки\U0001f379")
        ],
        [
            KeyboardButton(text="Главная\U00002B06")
        ]
    ],
    resize_keyboard=True
)
