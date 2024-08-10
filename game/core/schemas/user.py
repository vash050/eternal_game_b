from datetime import datetime
from typing import Optional

from fastapi_users import schemas

from core.types.user_id import UserIdType


class UserRead(schemas.BaseUser[UserIdType]):
    first_name: str
    last_name: str
    created_at: Optional[datetime]


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    last_name: str


class UserUpdate(schemas.BaseUserUpdate):
    first_name: str
    last_name: str
