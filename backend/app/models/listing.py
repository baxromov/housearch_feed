from typing import Optional
from datetime import datetime

from app.models.core import IDModelMixin, CoreModel


class ListingBase(CoreModel):
    id: int
    title: Optional[str] = None
    offering_type: Optional[str] = None
    agent_id: Optional[int] = None
    ref_num: Optional[str] = None
    updated_at: Optional[datetime] = None
    community_id: Optional[int] = None
    city: Optional[str] = None
    description: Optional[str] = None
    state: Optional[str] = None
    exclusivity: Optional[str] = None
    listing_type: Optional[str] = None
    furnished: Optional[bool] = None
    is_studio: Optional[bool] = None
    category: Optional[str] = None
    property_type_id: Optional[int] = None


class ListingInDB(IDModelMixin, ListingBase):
    id: int
    title: Optional[str] = None
    offering_type: Optional[str] = None
    agent_id: Optional[int] = None
    ref_num: Optional[str] = None
    updated_at: Optional[datetime] = None
    community_id: Optional[int] = None
    city: Optional[str] = None
    description: Optional[str] = None
    state: Optional[str] = None
    exclusivity: Optional[str] = None
    listing_type: Optional[str] = None
    furnished: Optional[bool] = None
    is_studio: Optional[bool] = None
    category: Optional[str] = None
    property_type_id: Optional[int] = None


class ListingPublic(IDModelMixin, ListingBase):
    pass
