from sqlalchemy import Column, Boolean
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from game.general.base import Base
from game import IdIntPkMixin


class UnitLevel(Base, IdIntPkMixin):
    name: Mapped[int]
    description: Mapped[str]
    bonus = Column(JSONB)
    max_experience: Mapped[int]
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
