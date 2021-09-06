from aiogram import Dispatcher

from bot.utils.states import SheduleStates

from .shedule import shedule_handler, set_shedule_handler, receive_shedule_handler, cancel_shedule_handler


def setup(dp: Dispatcher):
    dp.register_message_handler(shedule_handler, commands=["shedule"])
    dp.register_callback_query_handler(set_shedule_handler,
                                       lambda c: c.data == "set_shedule_yes",
                                       state="*")
    dp.register_callback_query_handler(cancel_shedule_handler,
                                       lambda c: c.data == "set_shedule_no",
                                       state="*")
    dp.register_message_handler(receive_shedule_handler, state=SheduleStates.receive_shedule)
