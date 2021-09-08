from aiohttp_apispec import json_schema, response_schema

from server.web.view import BaseView
from server.apps.bot_user.schema import (
    BotUserRegisterRequest,
    BotUserResponse,
    BotUser,
    BotUserSetSheduleRequest,
    BotUserTagsRequest,
    BotUserTagsResponse
)


class RegisterView(BaseView):
    @json_schema(BotUserRegisterRequest.Schema)
    @response_schema(BotUserResponse.Schema)
    async def post(self):
        user_data = self.request["json"]
        return await self.store.bot_user.register_user(user_data.user_id,
                                                       user_data.username)


class GetUserView(BaseView):
    @json_schema(BotUser.Schema)
    @response_schema(BotUserResponse.Schema)
    async def post(self):
        user_data = self.request["json"]
        return await self.store.bot_user.get_user(user_data.user_id)


class SetSheduleView(BaseView):
    @json_schema(BotUserSetSheduleRequest.Schema)
    @response_schema(BotUserResponse.Schema)
    async def post(self):
        user_data = self.request["json"]
        return await self.store.bot_user.set_shedule(user_data.user_id,
                                                     user_data.shedule)


class GetTagsView(BaseView):
    @json_schema(BotUser.Schema)
    @response_schema(BotUserTagsResponse.Schema)
    async def post(self):
        user_data = self.request["json"]
        return await self.store.bot_user.get_tags(user_data.user_id)


class AddTagsView(BaseView):
    @json_schema(BotUserTagsRequest.Schema)
    @response_schema(BotUserTagsResponse.Schema)
    async def post(self):
        user_data = self.request["json"]
        return await self.store.bot_user.add_tags(user_data.user_id,
                                                  user_data.tags)
