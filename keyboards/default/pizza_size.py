from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


pizza_size = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Маленькая"),
            KeyboardButton(text="Средная"),
            KeyboardButton(text="Большая")
        ],
        [
            KeyboardButton(text="Назад\U00002B05"),
            KeyboardButton(text="Главная\U00002B06")
        ]
    ],
    resize_keyboard=True
)
