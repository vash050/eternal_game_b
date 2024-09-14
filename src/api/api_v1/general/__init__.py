from fastapi import APIRouter

from core.config import settings
from .grade import router as grade_router
from .power_current import router as power_current_router
from .element import router as element_router

router = APIRouter(
    prefix=settings.api_prefix.v1.general,
    tags=["General"],
)
router.include_router(grade_router)
router.include_router(power_current_router)
router.include_router(element_router)
