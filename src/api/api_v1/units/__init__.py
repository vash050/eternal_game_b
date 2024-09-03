from fastapi import APIRouter

from core.config import settings
from .race import router as race_router
from .unit_level import router as unit_level_router

router = APIRouter(
    prefix=settings.api_prefix.v1.units,
    tags=["Units"],
)
router.include_router(race_router)
router.include_router(unit_level_router)
