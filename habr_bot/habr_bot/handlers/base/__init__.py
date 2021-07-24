from aiogram import Dispatcher
from aiogram.types import ContentTypes

from .base import (
    start_handler,
    file_handler
)


def setup(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start", "help"])
    dp.register_message_handler(file_handler, content_types=ContentTypes.DOCUMENT)
