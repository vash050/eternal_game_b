from datetime import datetime

from fastapi_users.db import (
    SQLAlchemyBaseUserTable,
)
from sqlalchemy import Column, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base


class User(Base, SQLAlchemyBaseUserTable[int]):
    first_name: Mapped[str]
    last_name: Mapped[str]
    created_at= mapped_column(DateTime(), server_default=func.now())
