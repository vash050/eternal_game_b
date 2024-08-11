from fastapi import (
    APIRouter,
    Depends,
)

from fastapi.security import HTTPBearer
from core.config import settings

from .auth import router as auth_router
from .users import router as users_router
from .messages import router as messages_router
from .units import router as units_router
from  .general import router as general_router

http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(
    prefix=settings.api_prefix.v1.prefix,
    dependencies=[Depends(http_bearer)],
)
router.include_router(auth_router)
router.include_router(users_router)
router.include_router(messages_router)
router.include_router(units_router)
router.include_router(general_router)

