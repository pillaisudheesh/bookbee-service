import os
from logger import logger


LOGGER = logger(__name__)


def get_bool_env(varname, default=False):
    return os.getenv(varname, 'TRUE' if default else 'FALSE').upper() == 'TRUE'


class Config(object):
    DEBUG = get_bool_env('DEBUG')
    FLASK_RUN_HOST = os.getenv('FLASK_RUN_HOST')
    FLASK_RUN_NO_RELOAD = os.getenv('FLASK_RUN_NO_RELOAD')
    FLASK_RUN_PORT = os.getenv('FLASK_RUN_PORT')


LOGGER.debug('*' * 50)
LOGGER.debug('Config.DEBUG: %s', Config.DEBUG)
LOGGER.debug('Config.FLASK_RUN_HOST: %s', Config.FLASK_RUN_HOST)
LOGGER.debug('Config.FLASK_RUN_NO_RELOAD: %s', Config.FLASK_RUN_NO_RELOAD)
LOGGER.debug('Config.FLASK_RUN_PORT: %s', Config.FLASK_RUN_PORT)
LOGGER.debug('*' * 50)