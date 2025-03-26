import logging
import logging.config

import pytest

from configuration import Configuration
from service import Service

logger = logging.getLogger(__name__)
configuration = Configuration()


@pytest.fixture(scope='session')
def service(request):

    return Service(configuration.service_url)

@pytest.fixture(scope='function', autouse=True)
def log_start_and_stop(request):
    logger.info(f'Starting test{request.node.nodeid}')
    yield
    logger.info(f'Stopping test{request.node.nodeid}')


@pytest.fixture(autouse=True)
def configure_logging():
    log_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'class': 'logging.Formatter',
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
        },
        'handlers': {
            'file_handler': {
                'class': 'logging.FileHandler',
                'filename': 'test.log',
                'mode': 'w',
                'encoding': 'utf-8',
                'formatter': 'standard'
            },
        },
        'loggers': {
            '': {
                'level': 'DEBUG',
                'handlers': ['file_handler']
            }
        }
    }
    logging.config.dictConfig(log_config)