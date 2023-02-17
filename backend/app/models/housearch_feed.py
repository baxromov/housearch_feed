# Default imports
from typing import Optional

from app.models.core import IDModelMixin, CoreModel


class PropertyTypeBase(CoreModel):
    title: Optional[str]
    bedrooms: Optional[int]
    bathrooms: Optional[int]


class PropertyTypeInDB(IDModelMixin, PropertyTypeBase):
    title: str
    bedrooms: int
    bathrooms: int


class PropertyTypePublic(IDModelMixin, PropertyTypeBase):
    pass
