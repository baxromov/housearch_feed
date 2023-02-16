import typing
from typing import List

from app.api.schemas.housearch_feed import data
from app.api.utils.dict2xml import dict_to_xml
from fastapi import APIRouter
from starlette.responses import Response

router = APIRouter()


class XmlResponse(Response):
    media_type = "text/xml"

    def render(self, content: typing.Any) -> bytes:
        return dict_to_xml({'response': content}).encode("utf-8")


@router.get("/")
async def get_feed() -> List[dict]:
    return XmlResponse(data)
