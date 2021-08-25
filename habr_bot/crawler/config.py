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
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": LOGGING_LEVEL,
            "formatter": "verbose",
            "filename": "crawler.log"
        }
    },
    "loggers": {
        "": {
            "handlers": ["console", "file"],
            "level": LOGGING_LEVEL,
            "propagate": False
        }
    },
    "disable_existing_loggers": True
}
