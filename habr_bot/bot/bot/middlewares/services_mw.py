from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message


class ServicesMiddleware(BaseMiddleware):
    def __init__(self, services: dict):
        super().__init__()
        self.services = services

    async def on_pre_process_message(self, _: Message, data: dict):
        data.update(self.services)
