from fastapi import APIRouter

from core.config import settings
from .grade import router as grade_router

router = APIRouter(
    prefix=settings.api_prefix.v1.general,
    tags=["General"],
)
router.include_router(grade_router)
