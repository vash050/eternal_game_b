from fastapi import APIRouter

from core.config import settings
from .race import router as race_router

router = APIRouter(
    prefix=settings.api_prefix.v1.units,
    tags=["Units"],
)
router.include_router(race_router)
