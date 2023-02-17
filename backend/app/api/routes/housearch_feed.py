import typing
from datetime import datetime
from typing import List

from app.api.schemas.housearch_feed import data, datum
from app.api.utils.dict2xml import dict_to_xml
from fastapi import APIRouter, Request, Body, Depends
from starlette.responses import Response

from app.models.housearch_feed import PropertyTypePublic, PropertyTypeBase
from app.db.repositories.housearch_feed import PropertyTypeRepository
from app.db.repositories.listing import ListingRepository
from app.api.dependencies.database import get_repository

router = APIRouter()


class XmlResponse(Response):
    media_type = "text/xml"

    def render(self, content: typing.Any) -> bytes:
        return dict_to_xml({'response': content}).encode("utf-8")


@router.get("/")
async def get_feed(request: Request,
                   listing: ListingRepository = Depends(get_repository(ListingRepository))):
    listing_query = await listing.get_listing()

    return XmlResponse(foo(listing_query))


def foo(query):
    listing = data
    listing_item = datum['realty-feed']
    listing_offer = datum['realty-feed']['offer']
    for item in query:
        listing_item['generation-date'] = datetime.now()
        listing_offer['@internal-id'] = item.ref_num
        listing_offer['category'] = item.category
        listing_offer['creation-date'] = item.updated_at
        listing['listing'].append(listing_item)
    return listing
