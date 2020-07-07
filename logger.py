import logging
from logging.config import fileConfig
import os


fileConfig('logging_config.ini')


def get_bool_env(varname, default=False):
    return os.getenv(varname, 'TRUE' if default else 'FALSE').upper() == 'TRUE'


def logger(module_name, level=logging.WARNING):
    console_handler = logging.getLogger().handlers[0]
    console_handler.setLevel(logging.DEBUG if get_bool_env('DEBUG') else level)
    logger_instance = logging.getLogger(module_name)
    return logger_instance


# Disable noisy libraries
logging.getLogger('faker').setLevel(logging.ERROR)
logging.getLogger('urllib3').setLevel(logging.ERROR)
logging.getLogger('passlib').setLevel(logging.ERROR)