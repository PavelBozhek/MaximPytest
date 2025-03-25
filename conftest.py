import pytest

from configuration import Configuration
from service import Service



configuration = Configuration()

@pytest.fixture(scope='session')
def service(request):

    return Service(configuration.service_url)