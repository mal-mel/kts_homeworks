import os


API_TOKEN = os.getenv("API_TOKEN")

LIMIT_REQUEST = 50


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
