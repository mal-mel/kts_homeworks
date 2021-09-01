import yaml
import os
import logging
import logging.config

from .services import RabbitInterface
from consumer import consumer

import config


def read_config(path: str) -> dict or None:
    if os.path.exists(path):
        with open(path) as cfg_file:
            return yaml.safe_load(cfg_file)


def init_logging():
    logging.config.dictConfig(config.LOGGER_CONFIG)


def init_rab_interface(_cfg: dict) -> RabbitInterface:
    return RabbitInterface(amqp_uri=_cfg["rabbit"]["uri"],
                           queue=_cfg["rabbit"]["queue"])


def init_postgre_interface(_cfg: dict):
    pass


if __name__ == '__main__':
    init_logging()
    cfg = read_config("config.yaml")
    if cfg:
        rab = init_rab_interface(cfg)
        postgre = init_postgre_interface(cfg)
        consumer(rab, postgre)
    else:
        logging.info("can't find config file")
