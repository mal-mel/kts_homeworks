import pathlib
import logging.config
import yaml


BASE_DIR = pathlib.Path(__file__).parent

dev_config_path = BASE_DIR / "config" / "config.yaml"
prod_config_path = BASE_DIR / "config" / "prod_config.yaml"


def read_config(path: str) -> dict:
    with open(path) as f:
        parsed_config = yaml.safe_load(f)
    return parsed_config


config = read_config(dev_config_path)


LOGGING_LEVEL = "DEBUG"

LOGGER_CONFIG = {
    "version": 1,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(module)s.%(funcName)s | %(asctime)s | %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": LOGGING_LEVEL,
            "formatter": "verbose"
        }
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": LOGGING_LEVEL,
            "propagate": False
        }
    },
    "disable_existing_loggers": True
}

logging.config.dictConfig(LOGGER_CONFIG)
