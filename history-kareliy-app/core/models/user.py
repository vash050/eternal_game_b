from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import (
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase,
)
from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from core.models.mixins.id_int_pk import IdIntPkMixin
from core.types.user_id import UserIdType

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[UserIdType]):
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    created_at = mapped_column(DateTime(), server_default=func.now())

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
