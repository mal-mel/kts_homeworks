import asyncio
import logging
import logging.config
import os
import yaml

import config

from crawler import Crawler
from crawler.services import ElasticInterface


def read_config(path: str) -> dict or None:
    if os.path.exists(path):
        with open(path) as cfg_file:
            return yaml.safe_load(cfg_file)


def init_logging():
    logging.config.dictConfig(config.LOGGER_CONFIG)


def init_crawler(_cfg: dict, es: ElasticInterface) -> Crawler:
    return Crawler(base_url=_cfg["crawler"]["url"],
                   workers_num=_cfg["crawler"]["workers"],
                   timeout=_cfg["crawler"]["timeout"],
                   elastic_interface=es)


def init_es_interface(_cfg: dict) -> ElasticInterface:
    return ElasticInterface(host=_cfg["elastic"]["host"],
                            port=_cfg["elastic"]["port"],
                            index=_cfg["elastic"]["index"])


async def main(_cfg: dict):
    es = init_es_interface(_cfg)
    crwl = init_crawler(_cfg, es)
    logging.info("start crawling")
    await crwl.start()
    logging.info("stop crawling")
    await crwl.stop()


if __name__ == '__main__':
    init_logging()
    cfg = read_config("config.yaml")
    if cfg:
        asyncio.run(main(cfg))
    else:
        logging.info("can't find config file")
