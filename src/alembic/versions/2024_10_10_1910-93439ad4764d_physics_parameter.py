"""physics_parameter

Revision ID: 93439ad4764d
Revises: 70a2afbb2ac2
Create Date: 2024-10-10 19:10:23.295181

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "93439ad4764d"
down_revision: Union[str, None] = "70a2afbb2ac2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "physics_parameters",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("grade", sa.Integer(), nullable=False),
        sa.Column("is_visibility", sa.Boolean(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("category", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["category"],
            ["power_currents.id"],
            name=op.f("fk_physics_parameters_category_power_currents"),
        ),
        sa.ForeignKeyConstraint(
            ["grade"],
            ["grades.id"],
            name=op.f("fk_physics_parameters_grade_grades"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_physics_parameters")),
    )


def downgrade() -> None:
    op.drop_table("physics_parameters")
