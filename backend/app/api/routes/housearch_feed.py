import typing
from typing import List

from app.api.schemas.housearch_feed import data
from app.api.utils.dict2xml import dict_to_xml
from fastapi import APIRouter, Request, Body, Depends
from starlette.responses import Response

from app.models.housearch_feed import PropertyTypePublic, PropertyTypeBase
from app.db.repositories.housearch_feed import PropertyTypeRepository
from app.api.dependencies.database import get_repository

router = APIRouter()


class XmlResponse(Response):
    media_type = "text/xml"

    def render(self, content: typing.Any) -> bytes:
        return dict_to_xml({'response': content}).encode("utf-8")


@router.get("/")
async def get_feed(request: Request,
                   property_type: PropertyTypeRepository = Depends(get_repository(PropertyTypeRepository))):
    property_type_query = await property_type.get_property_type()
    data['realty-feed']['offer']['bathrooms'] = property_type_query.bathrooms
    return XmlResponse(data)
