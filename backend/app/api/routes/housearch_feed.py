import typing
from datetime import datetime

from fastapi import APIRouter, Request, Depends
from starlette.responses import Response
import json
from app.api.dependencies.database import get_repository
from app.api.schemas.housearch_feed import data, datum
from app.api.utils.dict2xml import dict_to_xml
from app.db.repositories.listing import ListingRepository

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
    from pydantic.utils import deep_update
    listing = data
    listing_temp = datum['realty-feed']
    for item in query:
        room_space = [
            {
                'value': i.get('size', None),
                'unit': 'sqm'
            } for i in list(json.loads(item.size_rooms))] if item.size_rooms else [
            {
                'value': None,
                'unit': 'sqm'
            }]
        listing_new = {
            'generation-date': datetime.now(),
            'offer': {
                '@internal-id': item.ref_num,
                'category': item.category,
                'creation-date': item.updated_at,
                'location': {
                    'address': {
                        '@locale': 'en',
                        '#text': 'United Arab Emirates, Dubai, ,'
                    },
                    'latitude': item.lat,
                    'longitude': item.lon
                },
                'sales-agent': {
                    'name': item.full_name,
                    'image': item.photo
                },
                'price': {
                    'value': item.price,
                    'currency': 'AED'
                },
                'area': {
                    'value': item.size,
                    'unit': 'sqm'
                },
                'room-space': room_space,
                'rooms': len(json.loads(item.size_rooms)) if item.size_rooms else 0,
                'image': [
                    {
                        '@tag': 'plan',
                        '#text': 'http://www.developer.ru/images/plans/000001289.jpg'
                    },
                    'http://www.developer.ru/images/plans/0000013.jpg'
                ],
                'renovation': 'clean',
                'description': [
                    {
                        '@locale': 'ru',
                        '#text': item.description_ru
                    },
                    {
                        '@locale': 'en',
                        '#text': item.description_en
                    }
                ],
                'bedrooms': item.bedrooms,
                'bathrooms': item.bathrooms,
                'floor': '2',
                'floors-total': '5',
                'completion-year': '2020',
                'completion-quarter': '3',
                'lift': 'true',
                'ceiling-height': {
                    'value': '2.7',
                    'unit': 'meter'
                },
                'living-space': {
                    'value': '34.00',
                    'unit': 'sqm'
                },
                'kitchen-space': {
                    'value': '12',
                    'unit': 'sqm'
                }, 'balcony': '2',
                'studio': item.is_studio,
                'building-state': 'hand-over',
                'facility': ['gym', 'water pool', 'car charge', 'guarded building', 'parking']
            }
        }
        updated = deep_update(listing_temp, listing_new)
        listing['listing'].append(updated)
    return listing
