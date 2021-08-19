from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


pizza = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Средиземная'),
            KeyboardButton(text='Мексиканская'),
            KeyboardButton(text='Техас')
        ],
        [
            KeyboardButton(text='Фирменная Prosto'),
            KeyboardButton(text='Грибная'),
            KeyboardButton(text='Маргарита')
        ],
        [
            KeyboardButton(text='Мясная'),
            KeyboardButton(text='Чикен-Ранч'),
            KeyboardButton(text='Гавайская')
        ],
        [
            KeyboardButton(text='Назад\U00002B05'),
            KeyboardButton(text="Главная\U00002B06")
        ]
    ],
    resize_keyboard=True
)
