from app.db.repositories.base import BaseRepository
from app.models.housearch_feed import PropertyTypeInDB

GET_CLEANING_QUERY = """
    select id, title, bedrooms, bathrooms from property_types;
"""


class PropertyTypeRepository(BaseRepository):
    """"
        All database actions associated with the PropertyType resource
    """
    async def get_property_type(self, **kwargs) -> PropertyTypeInDB:
        # query_values = new_cleaning.dict()
        property_type = await self.db.fetch_all(query=GET_CLEANING_QUERY)
        return PropertyTypeInDB(**property_type[0])
