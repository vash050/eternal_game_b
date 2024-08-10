from sqlalchemy import Column, Boolean
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from units.models.mixins.id_int_mixin import IdIntPkMixin


class Race(Base, IdIntPkMixin):
    name: Mapped[str]
    description: Mapped[str]
    race_bonus = Column(JSONB)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)