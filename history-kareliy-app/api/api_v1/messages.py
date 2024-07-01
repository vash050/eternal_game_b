from fastapi import APIRouter
from fastapi import Depends

from core.config import settings

router = APIRouter(
    prefix=settings.api_prefix.v1.messages,
    tags=["Messages"],
)


def get_user_messages():
    pass
