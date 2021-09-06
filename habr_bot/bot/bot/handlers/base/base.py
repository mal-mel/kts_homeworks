from aiogram import types

import logging

from bot.services.admin_api import AdminAPIInterface
from bot.schemas import BotUserRegister

from . import templates


async def start_handler(message: types.Message, admin_api_obj: AdminAPIInterface):
    user_id, username = message.from_user.id, message.from_user.username
    user_data = BotUserRegister(
        user_id=user_id,
        username=username
    )
    resp = await admin_api_obj.register_bot_user(user_data)
    if resp.status == 200:
        logging.info(f"save new user: {user_data}")
        return await message.reply(templates.START_MESSAGE)
    if resp.status == 400:
        logging.info(f"user already registered: {user_data}")
        return await message.reply(templates.HELP_MESSAGE)
    return await message.reply(templates.ERROR_MESSAGE)


async def help_handler(mesage: types.Message):
    return await mesage.reply(templates.HELP_MESSAGE)
