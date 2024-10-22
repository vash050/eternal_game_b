"""body race

Revision ID: f32ba2db2a71
Revises: 93439ad4764d
Create Date: 2024-10-22 13:03:26.372527

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f32ba2db2a71"
down_revision: Union[str, None] = "93439ad4764d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "body_characteristics",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_body_characteristics")),
    )
    op.create_table(
        "body_energys",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_body_energys")),
    )
    op.create_table(
        "body_organs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("quantity_slots", sa.Integer(), nullable=False),
        sa.Column("size_slots", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_body_organs")),
    )
    op.create_table(
        "body_parts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("quantity_slots", sa.Integer(), nullable=False),
        sa.Column("size_slots", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_body_parts")),
    )
    op.create_table(
        "body_possible_states",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_body_possible_states")),
    )
    op.create_table(
        "body_races",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("quantity_parts_all", sa.Integer(), nullable=False),
        sa.Column("quantity_organs_all", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_body_races")),
    )
    op.create_table(
        "body_race_body_characteristic_association",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("body_race_id", sa.Integer(), nullable=False),
        sa.Column("body_characteristic_id", sa.Integer(), nullable=False),
        sa.Column("quantity_characteristic", sa.SMALLINT(), nullable=False),
        sa.ForeignKeyConstraint(
            ["body_characteristic_id"],
            ["body_characteristics.id"],
            name=op.f(
                "fk_body_race_body_characteristic_association_body_characteristic_id_body_characteristics"
            ),
        ),
        sa.ForeignKeyConstraint(
            ["body_race_id"],
            ["body_races.id"],
            name=op.f(
                "fk_body_race_body_characteristic_association_body_race_id_body_races"
            ),
        ),
        sa.PrimaryKeyConstraint(
            "id", name=op.f("pk_body_race_body_characteristic_association")
        ),
        sa.UniqueConstraint(
            "body_race_id",
            "body_characteristic_id",
            name="idx_unique_body_race_body_characteristic",
        ),
    )
    op.create_table(
        "body_race_body_energy_association",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("body_race_id", sa.Integer(), nullable=False),
        sa.Column("body_energy_id", sa.Integer(), nullable=False),
        sa.Column("quantity_body_energy", sa.SMALLINT(), nullable=False),
        sa.ForeignKeyConstraint(
            ["body_energy_id"],
            ["body_energys.id"],
            name=op.f(
                "fk_body_race_body_energy_association_body_energy_id_body_energys"
            ),
        ),
        sa.ForeignKeyConstraint(
            ["body_race_id"],
            ["body_races.id"],
            name=op.f(
                "fk_body_race_body_energy_association_body_race_id_body_races"
            ),
        ),
        sa.PrimaryKeyConstraint(
            "id", name=op.f("pk_body_race_body_energy_association")
        ),
        sa.UniqueConstraint(
            "body_race_id",
            "body_energy_id",
            name="idx_unique_body_race_body_energy",
        ),
    )
    op.create_table(
        "body_race_body_organ_association",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("body_race_id", sa.Integer(), nullable=False),
        sa.Column("body_organ_id", sa.Integer(), nullable=False),
        sa.Column("quantity_organs", sa.SMALLINT(), nullable=False),
        sa.ForeignKeyConstraint(
            ["body_organ_id"],
            ["body_organs.id"],
            name=op.f(
                "fk_body_race_body_organ_association_body_organ_id_body_organs"
            ),
        ),
        sa.ForeignKeyConstraint(
            ["body_race_id"],
            ["body_races.id"],
            name=op.f(
                "fk_body_race_body_organ_association_body_race_id_body_races"
            ),
        ),
        sa.PrimaryKeyConstraint(
            "id", name=op.f("pk_body_race_body_organ_association")
        ),
        sa.UniqueConstraint(
            "body_race_id",
            "body_organ_id",
            name="idx_unique_body_race_body_organ",
        ),
    )
    op.create_table(
        "body_race_body_part_association",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("body_race_id", sa.Integer(), nullable=False),
        sa.Column("body_part_id", sa.Integer(), nullable=False),
        sa.Column("quantity_parts", sa.SMALLINT(), nullable=False),
        sa.ForeignKeyConstraint(
            ["body_part_id"],
            ["body_parts.id"],
            name=op.f(
                "fk_body_race_body_part_association_body_part_id_body_parts"
            ),
        ),
        sa.ForeignKeyConstraint(
            ["body_race_id"],
            ["body_races.id"],
            name=op.f(
                "fk_body_race_body_part_association_body_race_id_body_races"
            ),
        ),
        sa.PrimaryKeyConstraint(
            "id", name=op.f("pk_body_race_body_part_association")
        ),
        sa.UniqueConstraint(
            "body_race_id",
            "body_part_id",
            name="idx_unique_body_race_body_parts",
        ),
    )
    op.create_table(
        "body_race_body_possible_state_association",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("body_race_id", sa.Integer(), nullable=False),
        sa.Column("body_possible_state_id", sa.Integer(), nullable=False),
        sa.Column("quantity_possible_states", sa.SMALLINT(), nullable=False),
        sa.ForeignKeyConstraint(
            ["body_possible_state_id"],
            ["body_possible_states.id"],
            name=op.f(
                "fk_body_race_body_possible_state_association_body_possible_state_id_body_possible_states"
            ),
        ),
        sa.ForeignKeyConstraint(
            ["body_race_id"],
            ["body_races.id"],
            name=op.f(
                "fk_body_race_body_possible_state_association_body_race_id_body_races"
            ),
        ),
        sa.PrimaryKeyConstraint(
            "id", name=op.f("pk_body_race_body_possible_state_association")
        ),
        sa.UniqueConstraint(
            "body_race_id",
            "body_possible_state_id",
            name="idx_unique_body_race_body_possible_state",
        ),
    )
    op.add_column("races", sa.Column("body", sa.Integer(), nullable=False))
    op.create_foreign_key(
        op.f("fk_races_body_body_races"),
        "races",
        "body_races",
        ["body"],
        ["id"],
    )


def downgrade() -> None:
    op.drop_constraint(
        op.f("fk_races_body_body_races"), "races", type_="foreignkey"
    )
    op.drop_column("races", "body")
    op.drop_table("body_race_body_possible_state_association")
    op.drop_table("body_race_body_part_association")
    op.drop_table("body_race_body_organ_association")
    op.drop_table("body_race_body_energy_association")
    op.drop_table("body_race_body_characteristic_association")
    op.drop_table("body_races")
    op.drop_table("body_possible_states")
    op.drop_table("body_parts")
    op.drop_table("body_organs")
    op.drop_table("body_energys")
    op.drop_table("body_characteristics")
