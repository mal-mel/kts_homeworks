from aiogram import Dispatcher

from tg_bot.utils.states import TagsStates

from .tags import tags_handler, tags_receive_handler


def setup(dp: Dispatcher):
    dp.register_message_handler(tags_handler, commands=["tags"], state="*")
    dp.register_message_handler(tags_receive_handler, state=TagsStates.receive_tags)
