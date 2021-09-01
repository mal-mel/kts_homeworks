from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Message


class ESMiddleware(BaseMiddleware):
    def __init__(self, es_obj):
        super().__init__()
        self.es_obj = es_obj

    async def on_pre_process_message(self, _: Message, data: dict):
        data["es_obj"] = self.es_obj
