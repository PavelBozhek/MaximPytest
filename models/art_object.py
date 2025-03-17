from pydantic import BaseModel, HttpUrl
from typing import Optional, Union

class ArtObject(BaseModel):
    objectID: int
    title: str
    artistDisplayName: Optional[str] = None
    objectDate: Optional[str] = None
    department: str
    primaryImage: Optional[Union[HttpUrl, str]] = None
