from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, SMALLINT, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from game import Base, IdIntPkMixin

if TYPE_CHECKING:
    from .material import Material
    from .element import Element


class MaterialElementAssociation(Base, IdIntPkMixin):
    __tablename__ = "material_element_association"
    __table_args__ = (
        UniqueConstraint(
            "material_id",
            "element_id",
            name="idx_unique_material_element",
        ),
    )

    material_id: Mapped[int] = mapped_column(ForeignKey("materials.id"))
    element_id: Mapped[int] = mapped_column(ForeignKey("elements.id"))
    quantity: Mapped[int] = mapped_column(SMALLINT, default=100, server_default="100")
    material: Mapped["Material"] = relationship(
        "Material", back_populates="element_details"
    )
    element: Mapped["Element"] = relationship(
        "Element", back_populates="material_details"
    )
