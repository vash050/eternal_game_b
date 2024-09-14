"""add material, association table

Revision ID: dde87526670a
Revises: a1c105e2c687
Create Date: 2024-09-14 14:16:09.147297

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "dde87526670a"
down_revision: Union[str, None] = "a1c105e2c687"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "materials",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("endurance", sa.SMALLINT(), nullable=False),
        sa.Column(
            "features", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.Column("img_url", sa.String(), nullable=False),
        sa.Column("grade_id", sa.Integer(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["grade_id"],
            ["grades.id"],
            name=op.f("fk_materials_grade_id_grades"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_materials")),
    )
    op.create_table(
        "material_element_association",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("material_id", sa.Integer(), nullable=False),
        sa.Column("element_id", sa.Integer(), nullable=False),
        sa.Column("quantity", sa.SMALLINT(), nullable=True),
        sa.ForeignKeyConstraint(
            ["element_id"],
            ["elements.id"],
            name=op.f("fk_material_element_association_element_id_elements"),
        ),
        sa.ForeignKeyConstraint(
            ["material_id"],
            ["materials.id"],
            name=op.f("fk_material_element_association_material_id_materials"),
        ),
        sa.PrimaryKeyConstraint(
            "id", name=op.f("pk_material_element_association")
        ),
        sa.UniqueConstraint(
            "material_id", "element_id", name="idx_unique_material_element"
        ),
    )


def downgrade() -> None:
    op.drop_table("material_element_association")
    op.drop_table("materials")
