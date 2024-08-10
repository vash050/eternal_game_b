from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends

from api.api_v1.fastapi_users_router import (
    current_user,
    current_superuser,
)

from core.config import settings
from core.models import User
from core.schemas.user import UserRead

router = APIRouter(
    prefix=settings.api_prefix.v1.messages,
    tags=["Messages"],
)


@router.get("")
def get_user_messages(
        user: Annotated[
            User,
            Depends(current_user),
        ],
):
    return {
        "message": ["m1", "m2", "m3", "m4", "m5"],
        "user": UserRead.model_validate(user),
    }


@router.get("/secrets")
def get_superuser_messages(
        user: Annotated[
            User,
            Depends(current_superuser),
        ],
):
    return {
        "message": ["secret-m1", "secret-m2", "secret-m3", "secret-m4", "secret-m5"],
        "user": UserRead.model_validate(user),
    }
