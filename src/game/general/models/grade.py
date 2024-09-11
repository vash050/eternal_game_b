from sqlalchemy import Column, Boolean
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from game import Base, IdIntPkMixin


# TODO: исправить race_bonus на grade_bonus
class Grade(Base, IdIntPkMixin):
    name: Mapped[str]
    description: Mapped[str]
    color: Mapped[str]
    race_bonus = Column(JSONB)
    img_url: Mapped[str]
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
