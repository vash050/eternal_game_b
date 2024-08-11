"""power current

Revision ID: b2b7d19b6464
Revises: bdc068e7f469
Create Date: 2024-08-11 21:58:05.814583

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "b2b7d19b6464"
down_revision: Union[str, None] = "bdc068e7f469"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "power_currents",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("color", sa.String(), nullable=False),
        sa.Column("img_url", sa.String(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_power_currents")),
    )


def downgrade() -> None:
    op.drop_table("power_currents")
