from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from bot.markups import get_tags_markup
from bot.services import AdminAPIInterface
from bot.utils.tg_api import get_bot_obj
from bot.schemas import BotUserRequest, BotUserAddTags
from bot.utils.states import TagsStates

from . import templates


async def tags_handler(message: types.Message, admin_api_obj: AdminAPIInterface):
    user_id = message.from_user.id
    user_data = BotUserRequest(user_id=user_id)
    resp = await admin_api_obj.get_tags(user_data)
    tags_markup = get_tags_markup()
    if resp.status == 200:
        tags = resp.data["tags"]
        return await message.reply(templates.CURRENT_TAGS.format(tags=" ".join(tags)),
                                   reply_markup=tags_markup,
                                   parse_mode="Markdown")
    if resp.status == 404:
        return await message.reply(templates.EMPTY_TAGS_MESSAGE,
                                   reply_markup=tags_markup)
    return await message.reply(templates.ERROR_MESSAGE)


async def set_tags_handler(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    bot = get_bot_obj()
    await bot.send_message(user_id, templates.ABOUT_MESSAGE, parse_mode="Markdown")
    await TagsStates.receive_tags.set()


async def cancel_tags_handler(callback_query: CallbackQuery, state: FSMContext):
    user_id = callback_query.from_user.id
    bot = get_bot_obj()
    await bot.send_message(user_id, templates.CANCEL_TAGS)
    return await state.finish()


async def tags_receive_handler(message: types.Message, state: FSMContext, admin_api_obj: AdminAPIInterface):
    tags = [tag.strip() for tag in message.text.split()]
    if not tags:
        return await message.reply(templates.MALFORMED_TAGS)

    user_id = message.from_user.id
    user_data = BotUserAddTags(
        user_id=user_id,
        tags=tags
    )
    resp = await admin_api_obj.add_tags(user_data)

    if resp.status == 200:
        await message.reply(templates.SUCCESS.format(tags=" ".join(tags)), parse_mode="Markdown")
        return await state.finish()
    return await message.reply(templates.ERROR_MESSAGE)
