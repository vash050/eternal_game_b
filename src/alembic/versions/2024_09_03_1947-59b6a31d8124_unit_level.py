"""unit_level

Revision ID: 59b6a31d8124
Revises: b2b7d19b6464
Create Date: 2024-09-03 19:47:26.116459

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "59b6a31d8124"
down_revision: Union[str, None] = "b2b7d19b6464"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "unit_levels",
        sa.Column(
            "bonus", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.Column("name", sa.Integer(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("max_experience", sa.Integer(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_unit_levels")),
    )


def downgrade() -> None:
    op.drop_table("unit_levels")
