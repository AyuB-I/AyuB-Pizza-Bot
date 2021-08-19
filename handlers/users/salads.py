from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default import salads, salad_quantity, home_page
from states.general import GeneralStates
from states.salads_menu import SaladsMenu
from config import URL_OLIVYE, URL_SEZAR


# Если в состоянии "menu" получен текст "Салаты" отправляем текст с кнопкой "салаты", устанавливаем состояние "салаты"
@dp.message_handler(text="Салаты\U0001F957", state=GeneralStates.menu)
async def choose_salad(message: types.Message):
    await message.answer(text="Выберите салат!", reply_markup=salads)
    await SaladsMenu.choosing_salad.set()


# Если выбрал "Оливье", отправляем текст с кнопкой "кол-во салата", устанавливаем состояние "количество салата"
@dp.message_handler(text="Оливье", state=SaladsMenu.choosing_salad)
async def choose_quantity(message: types.Message, state: FSMContext):
    await state.update_data(salad=message.text)
    await message.answer_photo(photo=URL_OLIVYE, caption="Оливье\n\nСостав:\n"
                                                         "колбаса, куринные яйца, зелёный горошек, солёный огурец, "
                                                         "картофель, морковь, майонез\n\n"
                                                         "Цена: 20.000 cум")
    await message.answer(text="Выберите количество!", reply_markup=salad_quantity)
    await SaladsMenu.choosing_quantity.set()


# Если выбрал "Цезарь", отправляем текст с кнопкой "кол-во салата", устанавливаем состояние "количество салата"
@dp.message_handler(text="Салат Цезарь", state=SaladsMenu.choosing_salad)
async def choose_quantity(message: types.Message, state: FSMContext):
    await state.update_data(salad=message.text)
    await message.answer_photo(photo=URL_SEZAR, caption="Салат Цезарь\n\nСостав:\n"
                                                        "Айсберг, сухарь, черри, пармезан, курица\n\n"
                                                        "Цена: 20.000 cум")
    await message.answer(text="Выберите количество!", reply_markup=salad_quantity)
    await SaladsMenu.choosing_quantity.set()


# Если состояние "выбор кол-ва", отправляем характеристику купленного салата и перекидываем в "главное меню"
@dp.message_handler(state=SaladsMenu.choosing_quantity)
async def choose_quantity(message: types.Message, state: FSMContext):
    await state.update_data(salad_quantity=message.text)
    data = await state.get_data()
    await message.answer(text="Спасибо за заказ!\U0001F60A")
    await message.answer(text=f"Вы заказывали:\n"
                              f"Салат - {data.get('salad')}\n"
                              f"Количество - {data.get('salad_quantity')}\n")
    await message.answer(text="Добавлено в Корзину\U0001F6D2", reply_markup=home_page)
    await state.finish()
