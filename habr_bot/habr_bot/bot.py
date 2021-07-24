from aiogram import Bot, Dispatcher, executor

from config import API_TOKEN
import handlers


_BOT = Bot(token=API_TOKEN)
_DP = Dispatcher(_BOT)


def start():
    handlers.base.setup(_DP)
    executor.start_polling(_DP, skip_updates=True)


if __name__ == '__main__':
    start()
