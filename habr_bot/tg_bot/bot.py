from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import os
import yaml
import logging.config

from config import API_TOKEN, LOGGER_CONFIG
from services import ElasticInterface
from middlewares import ESMiddleware

import handlers


BOT = Bot(token=API_TOKEN)
DP = Dispatcher(BOT, storage=MemoryStorage())


def read_config(path: str) -> dict or None:
    if os.path.exists(path):
        with open(path) as cfg_file:
            return yaml.safe_load(cfg_file)


def init_logging():
    logging.config.dictConfig(LOGGER_CONFIG)


def init_es_interface(_cfg: dict) -> ElasticInterface:
    return ElasticInterface(host=_cfg["elastic"]["host"],
                            port=_cfg["elastic"]["port"],
                            index=_cfg["elastic"]["index"])


def start(es_obj: ElasticInterface):
    handlers.base.setup(DP)
    handlers.tags.setup(DP)

    DP.middleware.setup(ESMiddleware(es_obj))

    executor.start_polling(DP, skip_updates=True, on_shutdown=shutdown)


async def shutdown(dp: Dispatcher):
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
    init_logging()
    cfg = read_config("config.yaml")
    if cfg:
        es = init_es_interface(cfg)
        start(es)
    else:
        logging.info("can't find config file")
