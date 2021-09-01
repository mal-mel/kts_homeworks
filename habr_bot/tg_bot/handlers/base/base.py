from aiogram import types

from . import templates


async def start_handler(message: types.Message):
    await message.reply(templates.START_MESSAGE)


async def help_handler(mesage: types.Message):
    await mesage.reply(templates.HELP_MESSAGE)
