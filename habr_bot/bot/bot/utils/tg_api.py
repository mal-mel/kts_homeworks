from aiogram import Bot

import io


def get_bot_obj() -> Bot:
    return Bot.get_current()


async def get_file_data(file_id: str) -> io.BytesIO:
    return await get_bot_obj().download_file_by_id(file_id)
