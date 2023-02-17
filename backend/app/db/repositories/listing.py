from app.db.repositories.base import BaseRepository
from app.models.listing import ListingInDB
import os

path = os.path.join(os.path.dirname(os.path.join(__file__)), 'sql/')

file = open('{}listing.sql'.format(path), 'r')
GET_CLEANING_QUERY = file.read()
file.close()


class ListingRepository(BaseRepository):
    """"
        All database actions associated with the PropertyType resource
    """

    async def get_listing(self, **kwargs) -> ListingInDB:
        listing = await self.db.fetch_all(query=GET_CLEANING_QUERY)
        return list(map(lambda x: ListingInDB(**x), listing))
