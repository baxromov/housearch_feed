from typing import Optional
from datetime import datetime

from app.models.core import IDModelMixin, CoreModel


class ListingBase(CoreModel):
    id: Optional[int] = None
    title: Optional[str] = None
    offering_type: Optional[str] = None
    ref_num: Optional[str] = None
    updated_at: Optional[datetime] = None
    city: Optional[str] = None
    description: Optional[str] = None
    listing_type: Optional[str] = None
    furnished: Optional[bool] = None
    is_studio: Optional[bool] = None
    category: Optional[str] = None
    address: Optional[str] = None
    lon: Optional[str] = None
    lat: Optional[str] = None
    bedrooms: Optional[int] = None
    bathrooms: Optional[int] = None
    full_name: Optional[str] = None  # sales-agent
    photo: Optional[str] = None
    price: Optional[float] = None
    size: Optional[float] = None


class ListingInDB(IDModelMixin, ListingBase):
    ...


class ListingPublic(IDModelMixin, ListingBase):
    pass
