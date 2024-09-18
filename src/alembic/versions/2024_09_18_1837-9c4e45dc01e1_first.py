"""first

Revision ID: 9c4e45dc01e1
Revises: 
Create Date: 2024-09-18 18:37:11.340859

"""

from typing import Sequence, Union

import fastapi_users_db_sqlalchemy
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "9c4e45dc01e1"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("first_name", sa.String(), nullable=True),
        sa.Column("last_name", sa.String(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=320), nullable=False),
        sa.Column("hashed_password", sa.String(length=1024), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("is_verified", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_users")),
    )
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=True)
    op.create_table(
        "access_tokens",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("token", sa.String(length=43), nullable=False),
        sa.Column(
            "created_at",
            fastapi_users_db_sqlalchemy.generics.TIMESTAMPAware(timezone=True),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name=op.f("fk_access_tokens_user_id_users"),
            ondelete="cascade",
        ),
        sa.PrimaryKeyConstraint("token", name=op.f("pk_access_tokens")),
    )
    op.create_index(
        op.f("ix_access_tokens_created_at"),
        "access_tokens",
        ["created_at"],
        unique=False,
    )
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
    op.create_table(
        "races",
        sa.Column(
            "race_bonus",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=True,
        ),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("img_url", sa.String(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_races")),
    )
    op.create_table(
        "unit_levels",
        sa.Column("bonus", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("name", sa.Integer(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("max_experience", sa.Integer(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_unit_levels")),
    )
    op.create_table(
        "elements",
        sa.Column("features", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("img_url", sa.String(), nullable=False),
        sa.Column("grade_id", sa.Integer(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["grade_id"],
            ["grades.id"],
            name=op.f("fk_elements_grade_id_grades"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_elements")),
    )
    op.create_table(
        "materials",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("endurance", sa.SMALLINT(), nullable=False),
        sa.Column("features", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("img_url", sa.String(), nullable=False),
        sa.Column("grade_id", sa.Integer(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["grade_id"],
            ["grades.id"],
            name=op.f("fk_materials_grade_id_grades"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_materials")),
    )
    op.create_table(
        "material_element_association",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("material_id", sa.Integer(), nullable=False),
        sa.Column("element_id", sa.Integer(), nullable=False),
        sa.Column("quantity", sa.SMALLINT(), server_default="100", nullable=False),
        sa.ForeignKeyConstraint(
            ["element_id"],
            ["elements.id"],
            name=op.f("fk_material_element_association_element_id_elements"),
        ),
        sa.ForeignKeyConstraint(
            ["material_id"],
            ["materials.id"],
            name=op.f("fk_material_element_association_material_id_materials"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_material_element_association")),
        sa.UniqueConstraint(
            "material_id", "element_id", name="idx_unique_material_element"
        ),
    )


def downgrade() -> None:
    op.drop_table("material_element_association")
    op.drop_table("materials")
    op.drop_table("elements")
    op.drop_table("unit_levels")
    op.drop_table("races")
    op.drop_table("power_currents")
    op.drop_table("grades")
    op.drop_index(op.f("ix_access_tokens_created_at"), table_name="access_tokens")
    op.drop_table("access_tokens")
    op.drop_index(op.f("ix_users_email"), table_name="users")
    op.drop_table("users")
