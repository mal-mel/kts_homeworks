from aiogram import types
from aiogram.dispatcher import FSMContext

from utils.states import TagsStates

from .templates import ABOUT_MESSAGE, MALFORMED_TAGS, SUCCESS


async def tags_handler(message: types.Message):
    await message.reply(ABOUT_MESSAGE, parse_mode="Markdown")
    await TagsStates.receive_tags.set()


async def tags_receive_handler(message: types.Message, state: FSMContext):
    tags = [tag.strip() for tag in message.text.split()]
    if not tags:
        await message.reply(MALFORMED_TAGS)
        return
    await message.reply(SUCCESS.format(tags=tags))
    await state.finish()
