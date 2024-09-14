"""element

Revision ID: a1c105e2c687
Revises: 59b6a31d8124
Create Date: 2024-09-11 17:54:17.423368

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "a1c105e2c687"
down_revision: Union[str, None] = "59b6a31d8124"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "elements",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("features", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("img_url", sa.String(), nullable=False),
        sa.Column("grade_id", sa.Integer(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ["grade_id"],
            ["grades.id"],
            name=op.f("fk_elements_grade_id_grades"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_elements")),
    )


def downgrade() -> None:
    op.drop_table("elements")
