from aiogram.dispatcher.filters.state import StatesGroup, State


class SaladsMenu(StatesGroup):
    choosing_salad = State()
    choosing_quantity = State()
