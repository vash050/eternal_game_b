"""unit, skill

Revision ID: 70a2afbb2ac2
Revises: 9c4e45dc01e1
Create Date: 2024-09-26 17:15:56.846988

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "70a2afbb2ac2"
down_revision: Union[str, None] = "9c4e45dc01e1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "skills",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("img_url", sa.String(), nullable=True),
        sa.Column(
            "skill_bonus",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=True,
        ),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_skills")),
    )
    op.create_table(
        "units",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("img_url", sa.String(), nullable=True),
        sa.Column("race", sa.Integer(), nullable=False),
        sa.Column("unit_level", sa.Integer(), nullable=False),
        sa.Column(
            "protection",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=False,
        ),
        sa.Column("damage", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column(
            "penetrate",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=False,
        ),
        sa.Column("speed_battle", sa.Float(), nullable=False),
        sa.Column("speed_travel", sa.Float(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ["race"], ["races.id"], name=op.f("fk_units_race_races")
        ),
        sa.ForeignKeyConstraint(
            ["unit_level"],
            ["unit_levels.id"],
            name=op.f("fk_units_unit_level_unit_levels"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_units")),
    )


def downgrade() -> None:
    op.drop_table("units")
    op.drop_table("skills")
