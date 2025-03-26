from typing import Any

from api.api import Api
from models.collection_objects import CollectionObjects
from service import Service


class CollectionObjectsV1(Api):
    def __init__(self, service: Service, code: int, params: dict[str, Any] | None = None):
        super().__init__(
            service=service,
            route="/objects",
            method="GET",
            model=CollectionObjects,
            params=params,
            code=code,
        )