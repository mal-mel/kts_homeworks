from aiogram import Dispatcher

from bot.utils.states import TagsStates

from .tags import (
    tags_handler,
    set_tags_handler,
    cancel_tags_handler,
    tags_receive_handler)


def setup(dp: Dispatcher):
    dp.register_message_handler(tags_handler, commands=["tags"])
    dp.register_callback_query_handler(set_tags_handler,
                                       lambda c: c.data == "set_tags_yes",
                                       state="*")
    dp.register_callback_query_handler(cancel_tags_handler,
                                       lambda c: c.data == "set_tags_no",
                                       state="*")
    dp.register_message_handler(tags_receive_handler, state=TagsStates.receive_tags)
