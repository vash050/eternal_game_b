from sqlalchemy import ForeignKey, UniqueConstraint, SMALLINT
from sqlalchemy.orm import Mapped, mapped_column

from game import IdIntPkMixin
from game.general.base import Base


class BodyRaceBodyPartAssociation(Base, IdIntPkMixin):
    __tablename__ = "body_race_body_part_association"
    __table_args__ = (
        UniqueConstraint(
            "body_race_id",
            "body_part_id",
            name="idx_unique_body_race_body_parts",
        ),
    )
    body_race_id: Mapped[int] = mapped_column(ForeignKey("body_races.id"))
    body_part_id: Mapped[int] = mapped_column(ForeignKey("body_parts.id"))
    quantity_parts: Mapped[int] = mapped_column(SMALLINT)
