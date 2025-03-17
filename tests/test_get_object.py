import requests
import pytest
import logging
from pydantic import ValidationError
from models.art_object import ArtObject

logging.basicConfig(level=logging.INFO)
BASE_URL = "https://collectionapi.metmuseum.org/public/collection/v1"


def test_get_valid_object():
    object_id = 437133
    response = requests.get(f"{BASE_URL}/objects/{object_id}")

    assert response.status_code == 200, "API не вернул 200 OK"
    try:
        ArtObject(**response.json())
    except ValidationError as e:
        pytest.fail(f"Ошибка валидации: {e}")

def test_get_object_with_logging():
    object_id = 437133
    url = f"{BASE_URL}/objects/{object_id}"

    logging.info(f"Запрос: {url}")
    response = requests.get(url)

    logging.info(f"Ответ ({response.status_code}): {response.text}")

    assert response.status_code == 200, "API не вернул 200 OK"