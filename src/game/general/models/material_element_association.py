from sqlalchemy import ForeignKey, SMALLINT, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from game import Base, IdIntPkMixin


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
    quantity: Mapped[int] = mapped_column(SMALLINT, default=100)
