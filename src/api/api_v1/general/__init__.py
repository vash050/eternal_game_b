from fastapi import APIRouter

from core.config import settings
from .grade import router as grade_router
from .power_current import router as power_current_router
from .element import router as element_router
from .material import router as material_router
from .physics_parameter import router as physics_parameter_router

router = APIRouter(
    prefix=settings.api_prefix.v1.general,
    tags=["General"],
)
router.include_router(grade_router)
router.include_router(power_current_router)
router.include_router(element_router)
router.include_router(material_router)
router.include_router(physics_parameter_router)
