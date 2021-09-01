from aiogram import Dispatcher

from .base import start_handler, help_handler


def setup(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])
    dp.register_message_handler(help_handler, commands=["help"])
