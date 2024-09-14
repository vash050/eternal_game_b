from sqlalchemy import Table, Column, ForeignKey, SMALLINT, Integer, UniqueConstraint

from game import Base

material_element_association_table = Table(
    "material_element_association",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("material_id", ForeignKey("materials.id"), nullable=False),
    Column("element_id", ForeignKey("elements.id"), nullable=False),
    Column("quantity", SMALLINT),
    UniqueConstraint("material_id", "element_id", name="idx_unique_material_element"),
)
