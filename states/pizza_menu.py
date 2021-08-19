from aiogram.dispatcher.filters.state import StatesGroup, State


class PizzaMenu(StatesGroup):
    choosing_pizza = State()
    choosing_size = State()
    choosing_quantity = State()
