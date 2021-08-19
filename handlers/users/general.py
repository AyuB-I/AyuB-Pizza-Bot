from loader import dp
from aiogram import types
from keyboards.default import home_page, menu
from aiogram.dispatcher import FSMContext
from states.general import GeneralStates


# Ловим кнопку(текст)"Главная" и отправляем текст прикрепляя кнопку home_page
@dp.message_handler(text="Главная\U00002B06", state="*")
async def cancel(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы заказать еду зайдите в Меню.', reply_markup=home_page)
    await state.finish()


# Ловим кнопку(текст)"Меню" и отправляем текст прикрепляя кнопку menu
@dp.message_handler(text='Меню\U0001F37D', state="*")
async def show_menu(message: types.Message):
    await message.answer(text="Что вы хотите?", reply_markup=menu)
    await GeneralStates.menu.set()
