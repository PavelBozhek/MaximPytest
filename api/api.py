import json
from typing import Any, Type

from pydantic import BaseModel

from service import Service


class Api:
    def __init__(self, service: Service, model: Type[BaseModel], route: str, method: str, code:int, params: dict[str, Any] | None = None,
                 body: dict[str, Any] | None = None):
        self.route = route
        self.method = method
        self.params = params
        self.body = body
        self.service = service
        self.model = model
        self.code = code

    def request(self):
        if self.params is None:
            self.params = {}

        response_text = self.service.request(method=self.method, route=self.route, params=self.params, body=self.body, code=self.code)
        if self.model and self.code == 200:
            response_json = json.loads(response_text)
            response = self.model(**response_json)
        else:
            response = response_text

        return response
