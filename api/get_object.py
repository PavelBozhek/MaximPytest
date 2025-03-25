from typing import Any

from api.api import Api
from models.art_object import ArtObject
from service import Service


class GetObject(Api):
    def __init__(self, service: Service, object_id, params: dict[str, Any] | None = None):
        super().__init__(
            service=service,
            route=f"objects/{object_id}",
            method="GET",
            model=ArtObject,
            params=params
        )