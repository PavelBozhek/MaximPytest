import requests
import pytest
import logging
from pydantic import ValidationError
from models.art_object import ArtObject

logging.basicConfig(level=logging.INFO)
BASE_URL = "https://collectionapi.metmuseum.org/public/collection/v1"

def test_search():
    query = "Van Gogh"
    response = requests.get(f"{BASE_URL}/search?q={query}")

    assert response.status_code == 200, "API не вернул 200 OK"

    data = response.json()
    assert "objectIDs" in data, "Ответ не содержит objectIDs"
    assert isinstance(data["objectIDs"], list), "objectIDs должен быть списком"
    assert len(data["objectIDs"]) > 0, "Поиск не нашел объекты"

    for object_id in data["objectIDs"][:5]:
        object_url = f"{BASE_URL}/objects/{object_id}"
        obj_response = requests.get(object_url).json()
        primary_image = obj_response.get("primaryImage", None)
        logging.info(f" Объект {object_id} - primaryImage: {primary_image}")

        assert primary_image and primary_image.strip(), f"Объект {object_id} не содержит изображения"