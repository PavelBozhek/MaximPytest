import logging
from typing import Any

import pytest
from requests import Request, Session, ConnectTimeout, RequestException

logger = logging.getLogger(__name__)


class Service:
    def __init__(self, url: str):
        self.url = url

    def request(self, method: str, route: str, code: int, params: dict[str, Any], body: dict[str, Any] | None = None):
        url = f"{self.url}/{route}"
        request = Request(method, url, params=params, json=body).prepare()

        logger.info(f"Request:{method} {url}")
        logger.info(f"Body:{body}")

        session = Session()
        try:
            response = session.send(request, timeout=10.0)
            assert response.status_code == code
            logger.info(f"Response:{response.status_code} {response.text}")
            return str(response.text)
        except ConnectTimeout as e:
            logger.info(f"Response:{url} {e}")
            pytest.fail("Timeout error")
        except RequestException as e:
            logger.info(f"Response:{url} {e}")
            pytest.fail("Request error")
