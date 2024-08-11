"""grade

Revision ID: d49db257bb55
Revises: 9452128df385
Create Date: 2024-08-11 15:13:32.236507

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "d49db257bb55"
down_revision: Union[str, None] = "9452128df385"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "grades",
        sa.Column(
            "race_bonus",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=True,
        ),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("color", sa.String(), nullable=False),
        sa.Column("img_url", sa.String(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_grades")),
    )


def downgrade() -> None:
    op.drop_table("grades")
