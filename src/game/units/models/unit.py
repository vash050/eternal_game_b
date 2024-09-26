from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Column, Float
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from game import IdIntPkMixin
from game.general.base import Base

if TYPE_CHECKING:
    from .skill import Skill


class Unit(Base, IdIntPkMixin):
    name: Mapped[str]
    description: Mapped[str]
    img_url: Mapped[str | None]
    race: Mapped[int] = mapped_column(ForeignKey("races.id"))
    unit_level: Mapped[int] = mapped_column(ForeignKey("unit_levels.id"))
    protection: Mapped[dict[str, int]] = mapped_column(JSONB)
    damage: Mapped[dict[str, int]] = mapped_column(JSONB)
    penetrate: Mapped[dict[str, int]] = mapped_column(JSONB)
    speed_battle: Mapped[float] = mapped_column(Float, default=1.0)
    speed_travel: Mapped[float] = mapped_column(Float, default=1.0)
    is_active: Mapped[bool]
    # main_parameters: Mapped[list["MainParameters"]] = relationship(
    #     back_populates="units",
    #     secondary="unit_main_parameters_association",
    # )
    skills: Mapped[list["Skill"]] = relationship(
        back_populates="units",
        secondary="unit_skill_association",
    )
    # hidden_parameters: Mapped[list["HiddenParameters"]] = relationship(
    #     back_populates="units",
    #     secondary="unit_hidden_parameters_association",
    # )
