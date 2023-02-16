from fastapi import APIRouter
from app.api.routes.housearch_feed import router as get_feed_router

router = APIRouter()
router.include_router(get_feed_router, prefix="/feed", tags=["cleanings"])
