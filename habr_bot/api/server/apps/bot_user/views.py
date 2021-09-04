from aiohttp_apispec import json_schema, response_schema

from server.web.view import BaseView
from server.apps.bot_user.schema import BotUserRegisterRequest, BotUserResponse


class BotUserRegisterView(BaseView):
    @json_schema(BotUserRegisterRequest.Schema)
    @response_schema(BotUserResponse.Schema)
    async def post(self):
        user_data = self.request["json"]
        return await self.store.bot_user.register_user(user_data.user_id,
                                                       user_data.chat_id,
                                                       user_data.username)
