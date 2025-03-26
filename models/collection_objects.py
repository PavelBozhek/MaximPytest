from pydantic import BaseModel, Field


class CollectionObjects(BaseModel, extra='forbid'):
    total: int
    object_ids: list[int] = Field(alias='objectIDs')