import aiohttp

from urllib.parse import urljoin

from tg_bot.schema.schema import UserBotRegister


class AdminAPIInterface:
    def __init__(self, host: str, port: int):
        self.host, self.port = host, port
        self.url = "http://" + host.strip("/") + f":{port}"
        self._session = aiohttp.ClientSession()

    async def register_bot_user(self, user_data: UserBotRegister) -> tuple:
        json_data = user_data.Schema().dump(user_data)
        url = urljoin(self.url, "/bot_user.register")
        async with self._session.post(url, json=json_data) as response:
            return await response.json(), response.status

    def close(self):
        self._session.close()
