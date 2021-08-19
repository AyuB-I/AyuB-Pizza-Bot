from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


salads = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Оливье"),
            KeyboardButton(text="Салат Цезарь")
        ],
        [
            KeyboardButton(text="Назад\U00002B05"),
            KeyboardButton(text="Главная\U00002B06")
        ]
    ],
    resize_keyboard=True
)
