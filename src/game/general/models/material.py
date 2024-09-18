from __future__ import annotations

from typing import TYPE_CHECKING
from sqlalchemy import Column, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB, SMALLINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from game import Base, IdIntPkMixin

if TYPE_CHECKING:
    from .element import Element
    from .material_element_association import MaterialElementAssociation


class Material(Base, IdIntPkMixin):
    name: Mapped[str]
    description: Mapped[str]
    element_details: Mapped[list["MaterialElementAssociation"]] = relationship(
        back_populates="material"
    )
    endurance: Mapped[int] = mapped_column(SMALLINT, default=100)
    features = Column(JSONB)
    img_url: Mapped[str]
    grade_id: Mapped[int] = mapped_column(ForeignKey("grades.id"))
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
