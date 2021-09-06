from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.services import AdminAPIInterface
from bot.schemas import BotUserRequest
from bot.utils.states import TagsStates

from . import templates


async def tags_handler(message: types.Message, admin_api_obj: AdminAPIInterface):
    user_id = message.from_user.id
    user_data = BotUserRequest(user_id=user_id)
    resp = await admin_api_obj.get_tags(user_data)
    if resp.status == 200:
        tags = resp.data['tags']
        await message.reply(templates.CURRENT_TAGS.format(tags=" ".join(tags)))
    else:
        await message.reply(templates.ABOUT_MESSAGE, parse_mode="Markdown")
    await TagsStates.receive_tags.set()


async def tags_receive_handler(message: types.Message, state: FSMContext):
    tags = [tag.strip() for tag in message.text.split()]
    if not tags:
        return await message.reply(templates.MALFORMED_TAGS)
    await message.reply(templates.SUCCESS.format(tags=" ".join(tags)))
    await state.finish()
