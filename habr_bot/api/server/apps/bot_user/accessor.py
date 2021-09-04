from server.apps.bot_user.models import BotUser
from server.store.accessor import Accessor
from server.web.exceptions import AlreadyExists


class BotUserAccessor(Accessor):
    @staticmethod
    async def register_user(user_id: int, chat_id: int, username: str) -> BotUser:
        user = await BotUser.query.where(BotUser.user_id == user_id).gino.first()
        if user is not None:
            raise AlreadyExists
        return await BotUser.create(user_id=user_id, chat_id=chat_id, username=username)
