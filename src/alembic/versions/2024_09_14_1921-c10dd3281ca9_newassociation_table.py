"""newassociation table

Revision ID: c10dd3281ca9
Revises: dde87526670a
Create Date: 2024-09-14 19:21:54.787705

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c10dd3281ca9"
down_revision: Union[str, None] = "dde87526670a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "material_element_association",
        "quantity",
        existing_type=sa.SMALLINT(),
        nullable=False,
    )


def downgrade() -> None:
    op.alter_column(
        "material_element_association",
        "quantity",
        existing_type=sa.SMALLINT(),
        nullable=True,
    )
