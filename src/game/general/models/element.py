from __future__ import annotations

from typing import TYPE_CHECKING
from sqlalchemy import Column, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from game import Base, IdIntPkMixin

if TYPE_CHECKING:
    from .material import Material


class Element(Base, IdIntPkMixin):
    name: Mapped[str]
    description: Mapped[str]
    features = Column(JSONB)
    img_url: Mapped[str]
    grade_id: Mapped[int] = mapped_column(ForeignKey("grades.id"))
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
    materials: Mapped[list[Material]] = relationship(
        secondary="material_element_association_table",
        back_populates="elements",
    )
