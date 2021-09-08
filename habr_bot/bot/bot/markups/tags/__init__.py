from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_tags_markup() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    yes_btn = InlineKeyboardButton("Да", callback_data="set_tags_yes")
    no_btn = InlineKeyboardButton("Нет", callback_data="set_tags_no")
    keyboard.add(yes_btn)
    keyboard.add(no_btn)
    return keyboard
