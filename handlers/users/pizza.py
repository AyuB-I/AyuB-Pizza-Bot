from config import URL_MENU
from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default import pizza, pizza_size, pizza_quantity, home_page
from states.general import GeneralStates
from states.pizza_menu import PizzaMenu


# Если в состоянии "меню" получен текст "Пицца" отправляем текст с кнопкой "пицца", устанавливаем состояние "пицца"
@dp.message_handler(text="Пицца\U0001f355", state=GeneralStates.menu)
async def choose_pizza(message: types.Message):
    await message.answer(text='Выберите пиццу!', reply_markup=pizza)
    await message.answer_photo(URL_MENU)
    await PizzaMenu.choosing_pizza.set()


# Если состояние "выбор пиццы", отправляем текст с кнопкой "размер пиццы", устанавливаем состояние "выбор размера"
@dp.message_handler(state=PizzaMenu.choosing_pizza)
async def choose_size(message: types.Message, state: FSMContext):
    await state.update_data(pizza=message.text)
    await message.answer(text="Выберите размер!", reply_markup=pizza_size)
    await PizzaMenu.choosing_size.set()


# Если состояние "выбор размера", отправляем текст с кнопкой "кол-во пиццы", устанавливаем состояние "выбор количества"
@dp.message_handler(state=PizzaMenu.choosing_size)
async def choose_quantity(message: types.Message, state: FSMContext):
    await state.update_data(pizza_size=message.text)
    await message.answer(text="Выберите количество!", reply_markup=pizza_quantity)
    await PizzaMenu.choosing_quantity.set()


# Если состояние "выбор количества", отправляем характеристику купленной пиццы и перекидываем в "главное меню"
@dp.message_handler(state=PizzaMenu.choosing_quantity)
async def complete_order_pizza(message: types.Message, state: FSMContext):
    await state.update_data(pizza_quantity=message.text)
    data = await state.get_data()
    await message.answer(text="Спасибо за заказ!\U0001F60A")
    await message.answer(text=f"Вы заказывали:\n"
                              f"Пицца - {data.get('pizza')}\n"
                              f"Размер - {data.get('pizza_size')}\n"
                              f"Количество - {data.get('pizza_quantity')}\n")
    await message.answer(text="Добавлено в Корзину\U0001F6D2", reply_markup=home_page)
    await state.finish()
