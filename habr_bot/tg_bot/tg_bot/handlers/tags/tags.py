from aiogram import types
from aiogram.dispatcher import FSMContext

from tg_bot.utils.states import TagsStates

from . import templates


async def tags_handler(message: types.Message):
    await message.reply(templates.ABOUT_MESSAGE, parse_mode="Markdown")
    await TagsStates.receive_tags.set()


async def tags_receive_handler(message: types.Message, state: FSMContext):
    tags = [tag.strip() for tag in message.text.split()]
    if not tags:
        await message.reply(templates.MALFORMED_TAGS)
        return
    await message.reply(templates.SUCCESS.format(tags=tags))
    await state.finish()
