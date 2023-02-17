from typing import Optional
from enum import Enum
from app.models.core import IDModelMixin, CoreModel


class ListingBase(CoreModel):
    title: str
    offering_type: str
    agent_id: int
    ref_num: int
    updated_at: str
    community_id: int
    city: str
    description: str
    state: str
    exclusivity: str
    listing_type: str
    furnished: bool
    is_studio: bool
    category: str
    property_type_id: int


class ListingInDB(IDModelMixin, ListingBase):
    title: str
    offering_type: str
    agent_id: int
    ref_num: int
    updated_at: str
    community_id: int
    city: str
    description: str
    state: str
    exclusivity: str
    listing_type: str
    furnished: bool
    is_studio: bool
    category: str
    property_type_id: int


class ListingPublic(IDModelMixin, ListingBase):
    pass
