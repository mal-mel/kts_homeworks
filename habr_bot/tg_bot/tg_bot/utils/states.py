from aiogram.dispatcher.filters.state import StatesGroup, State


class TagsStates(StatesGroup):
    receive_tags = State()
