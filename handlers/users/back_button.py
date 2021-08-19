from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default import home_page, menu, pizza, pizza_size, salads
from states.general import GeneralStates
from states.pizza_menu import PizzaMenu
from states.salads_menu import SaladsMenu


# Ловим кнопку(текст)"Назад" в меню и перекидываем в главную меню
@dp.message_handler(text="Назад\U00002B05", state=GeneralStates.menu)
async def cancel(message: types.Message, state: FSMContext):
    await message.answer(text="Чтобы заказать еду зайдите в Меню.", reply_markup=home_page)
    await state.finish()


# Ловим кнопку(текст)"Назад" при выборе пиццы и перекидываем в меню
@dp.message_handler(text="Назад\U00002B05", state=PizzaMenu.choosing_pizza)
async def cancel(message: types.Message):
    await message.answer(text="Что вы хотите?", reply_markup=menu)
    await GeneralStates.menu.set()


# Ловим кнопку(текст)"Назад" при выборе размера и перекидываем в выбор пиццы
@dp.message_handler(text="Назад\U00002B05", state=PizzaMenu.choosing_size)
async def cancel(message: types.Message):
    await message.answer(text="Выберите пиццу!", reply_markup=pizza)
    await PizzaMenu.choosing_pizza.set()


# Ловим кнопку(текст)"Назад" при выборе количества и перекидываем в выбор размера
@dp.message_handler(text="Назад\U00002B05", state=PizzaMenu.choosing_quantity)
async def cancel(message: types.Message):
    await message.answer(text="Выберите размер!", reply_markup=pizza_size)
    await PizzaMenu.choosing_size.set()


# Ловим кнопку(текст)"Назад" при выборе салата и перекидываем в меню
@dp.message_handler(text="Назад\U00002B05", state=SaladsMenu.choosing_salad)
async def cancel(message: types.Message):
    await message.answer(text="Что вы хотите?", reply_markup=menu)
    await GeneralStates.menu.set()


# Ловим кнопку(текст)"Назад" при выборе количества и перекидываем в выбор салата
@dp.message_handler(text="Назад\U00002B05", state=PizzaMenu.choosing_quantity)
async def cancel(message: types.Message):
    await message.answer(text="Выберите салат!", reply_markup=salads)
    await SaladsMenu.choosing_salad.set()
