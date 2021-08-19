from aiogram.dispatcher.filters import CommandStart
from aiogram import types
from keyboards.default import home_page
from loader import dp
from sqlighter import SQLighter

# Инициализируем соединение с БД
db = SQLighter("db.db")


# Обработка команды "старт"
@dp.message_handler(CommandStart())
async def on_start(message: types.Message):
    await message.answer(f'Aссаламу Алайкум {message.from_user.full_name}!\n\nЯ БОТ пиццерии "AyuB\'s Pizza"',
                         reply_markup=home_page)

    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id, message.from_user.username, message.from_user.full_name)

    else:
        db.update_status(message.from_user.id, True)

    print(db.user_exists(message.from_user.id))  # Что-бы узнать работает ли функция
