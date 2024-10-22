"""fix models

Revision ID: 36b612c8d656
Revises: e81c96c4d7d5
Create Date: 2024-10-22 16:54:43.164649

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "36b612c8d656"
down_revision: Union[str, None] = "e81c96c4d7d5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint(
        "idx_unique_body_race_body_characteristic",
        "body_race_body_characteristic_association",
        type_="unique",
    )
    op.create_unique_constraint(
        "idx_unique_body_race_characteristic",
        "body_race_body_characteristic_association",
        ["body_race_id", "body_characteristic_id"],
    )
    op.add_column(
        "body_race_body_energy_association",
        sa.Column("energy_id", sa.Integer(), nullable=False),
    )
    op.drop_constraint(
        "idx_unique_body_race_body_energy",
        "body_race_body_energy_association",
        type_="unique",
    )
    op.create_unique_constraint(
        "idx_unique_body_race_body_energy",
        "body_race_body_energy_association",
        ["body_race_id", "energy_id"],
    )
    op.drop_constraint(
        "fk_body_race_body_energy_association_body_energy_id_bod_2013",
        "body_race_body_energy_association",
        type_="foreignkey",
    )
    op.create_foreign_key(
        op.f("fk_body_race_body_energy_association_energy_id_energys"),
        "body_race_body_energy_association",
        "energys",
        ["energy_id"],
        ["id"],
    )
    op.drop_column("body_race_body_energy_association", "body_energy_id")


def downgrade() -> None:
    op.add_column(
        "body_race_body_energy_association",
        sa.Column("body_energy_id", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.drop_constraint(
        op.f("fk_body_race_body_energy_association_energy_id_energys"),
        "body_race_body_energy_association",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "fk_body_race_body_energy_association_body_energy_id_bod_2013",
        "body_race_body_energy_association",
        "body_energys",
        ["body_energy_id"],
        ["id"],
    )
    op.drop_constraint(
        "idx_unique_body_race_body_energy",
        "body_race_body_energy_association",
        type_="unique",
    )
    op.create_unique_constraint(
        "idx_unique_body_race_body_energy",
        "body_race_body_energy_association",
        ["body_race_id", "body_energy_id"],
    )
    op.drop_column("body_race_body_energy_association", "energy_id")
    op.drop_constraint(
        "idx_unique_body_race_characteristic",
        "body_race_body_characteristic_association",
        type_="unique",
    )
    op.create_unique_constraint(
        "idx_unique_body_race_body_characteristic",
        "body_race_body_characteristic_association",
        ["body_race_id", "body_characteristic_id"],
    )
