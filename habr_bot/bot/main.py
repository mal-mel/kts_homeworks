from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import os
import yaml
import logging.config

from config import API_TOKEN, LOGGER_CONFIG
from bot.services import ElasticInterface
from bot.services import AdminAPIInterface
from bot.middlewares import ServicesMiddleware
from bot import handlers


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


def init_admin_api_interface(_cfg: dict) -> AdminAPIInterface:
    return AdminAPIInterface(host=_cfg["admin_api"]["host"],
                             port=_cfg["admin_api"]["port"])


def start(es_obj: ElasticInterface, admin_api_obj: AdminAPIInterface):
    handlers.base.setup(DP)
    handlers.tags.setup(DP)
    handlers.shedule.setup(DP)

    DP.middleware.setup(ServicesMiddleware({
        "es_obj": es_obj,
        "admin_api_obj": admin_api_obj
    }))

    executor.start_polling(DP, skip_updates=True, on_shutdown=shutdown)


async def shutdown(dp: Dispatcher):
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
    init_logging()
    cfg = read_config("config/config.yaml")
    if cfg:
        es = init_es_interface(cfg)
        admin_api = init_admin_api_interface(cfg)
        start(es, admin_api)
    else:
        logging.info("can't find config file")
