select l.id,
       l.title,
       l.offering_type,
       l.ref_num,
       l.updated_at,
       l.city,
       l.description_ru,
       l.description_en,
       l.listing_type,
       l.furnished,
       l.is_studio,
       l.category,
       c.address,
       c.lon,
       c.lat,
       pt.bedrooms,
       pt.bathrooms,
       u.full_name,
       u.photo,
       pt.price,
       pt.size /* area */,
       pt.size_rooms
from listing l
join community c on l.community_id = c.id
join property_types as pt on pt.id = l.property_type_id
join "user"  u on u.id = l.agent_id
where l.city like '%Dubai%'
  and l.listing_type = 'axcapital'
  and l.state = 'APPROVED';
