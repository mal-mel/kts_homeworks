import aiohttp

from urllib.parse import urljoin

from bot.schemas import (
    BotUserRegister,
    BotUserSetShedule,
    BotUserRequest,
    BotUserAddTags,
    BaseResponse
)


class HttpClient:
    def __init__(self, host: str, port: int):
        self.host, self.port = host, port
        self.url = "http://" + host.strip("/") + f":{port}"
        self._session = aiohttp.ClientSession()

    async def _post(self, url: str, data: dict) -> BaseResponse:
        async with self._session.post(url, json=data) as response:
            resp_json = await response.json()
            if response.status == 200:
                resp_json = resp_json["data"]
            return BaseResponse(status=response.status, data=resp_json)

    def close(self):
        self._session.close()


class AdminAPIInterface(HttpClient):
    async def register_bot_user(self, user_data: BotUserRegister) -> BaseResponse:
        url = urljoin(self.url, "/bot_user/register")
        return await self._post(url, user_data.json)

    async def set_shedule(self, user_data: BotUserSetShedule) -> BaseResponse:
        url = urljoin(self.url, "/bot_user/set_shedule")
        return await self._post(url, user_data.json)

    async def get_user(self, user_data: BotUserRequest) -> BaseResponse:
        url = urljoin(self.url, "/bot_user/get")
        return await self._post(url, user_data.json)

    async def add_tags(self, user_data: BotUserAddTags) -> BaseResponse:
        url = urljoin(self.url, "/bot_user/add_tags")
        return await self._post(url, user_data.json)

    async def get_tags(self, user_data: BotUserRequest) -> BaseResponse:
        url = urljoin(self.url, "/bot_user/get_tags")
        return await self._post(url, user_data.json)
