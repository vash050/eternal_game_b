"""energy

Revision ID: e81c96c4d7d5
Revises: f32ba2db2a71
Create Date: 2024-10-22 16:36:08.240241

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e81c96c4d7d5"
down_revision: Union[str, None] = "f32ba2db2a71"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "energys",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("color", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_energys")),
    )


def downgrade() -> None:
    op.drop_table("energys")
