from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from dateutil import parser as dt_parser

import logging

from bot.markups import get_shedule_markup
from bot.services import AdminAPIInterface
from bot.utils.states import SheduleStates
from bot.utils.tg_api import get_bot_obj
from bot.utils.validators import validate_time
from bot.schemas import BotUserSetShedule, BotUserRequest

from . import templates


async def shedule_handler(message: Message, admin_api_obj: AdminAPIInterface):
    user_id = message.from_user.id
    user_data = BotUserRequest(user_id=user_id)
    logging.info(f"get shedule for user: {user_data}")
    resp = await admin_api_obj.get_user(user_data)
    if resp.status == 200:
        current_shedule = resp.data.get("shedule")
        shedule_markup = get_shedule_markup()
        logging.info(f"current shedule {current_shedule} for user: {user_data}")
        if current_shedule:
            return await message.reply(templates.CURRENT_SHEDULE.format(shedule=resp.data["shedule"]),
                                       reply_markup=shedule_markup,
                                       parse_mode="Markdown")
        return await message.reply(templates.EMPTY_SHEDULE, reply_markup=shedule_markup)
    return await message.reply(templates.ERROR_MESSAGE)


async def cancel_shedule_handler(callback_query: CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    bot = get_bot_obj()
    await bot.send_message(user_id, templates.CANCEL_SHEDULE)
    return await state.finish()


async def set_shedule_handler(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    bot = get_bot_obj()
    await bot.send_message(user_id, templates.RECEIVE_SHEDULE, parse_mode="Markdown")
    await SheduleStates.receive_shedule.set()


async def receive_shedule_handler(message: Message, state: FSMContext, admin_api_obj: AdminAPIInterface):
    user_id = message.from_user.id
    time_s = message.text.strip()
    if not validate_time(time_s):
        return await message.reply(templates.MALFORMED_SHEDULE)
    user_data = BotUserSetShedule(
        user_id=user_id,
        shedule=dt_parser.parse(time_s).time()
    )
    logging.info(f"set new shedule for user: {user_data}")
    resp = await admin_api_obj.set_shedule(user_data)
    if resp.status == 200:
        await message.reply(templates.SUCCESS_SHEDULE.format(shedule=time_s), parse_mode="Markdown")
        return await state.finish()
    return await message.reply(templates.ERROR_MESSAGE)
