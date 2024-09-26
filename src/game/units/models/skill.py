from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from game.general.base import Base
from game import IdIntPkMixin

if TYPE_CHECKING:
    from .unit import Unit


class Skill(Base, IdIntPkMixin):
    name: Mapped[str]
    description: Mapped[str]
    img_url: Mapped[str | None]
    skill_bonus: Mapped[dict[str, float]] | None = Column(JSONB)
    # магия, физика и т.д.
    units: Mapped["Unit"] = relationship(
        back_populates="skills",
        secondary="unit_skill_association",
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)

