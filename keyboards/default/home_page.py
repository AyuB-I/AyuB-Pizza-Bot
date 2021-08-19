from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


home_page = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Меню\U0001F37D')
        ],
        [
            KeyboardButton(text='Корзина\U0001F6D2'),
            KeyboardButton(text='Настройки\U00002699')
        ]
    ],
    resize_keyboard=True
)

