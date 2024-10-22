from sqlalchemy import ForeignKey, UniqueConstraint, SMALLINT
from sqlalchemy.orm import Mapped, mapped_column

from game import IdIntPkMixin
from game.general.base import Base


class BodyRaceBodyOrganAssociation(Base, IdIntPkMixin):
    __tablename__ = "body_race_body_organ_association"
    __table_args__ = (
        UniqueConstraint(
            "body_race_id",
            "body_organ_id",
            name="idx_unique_body_race_body_organ",
        ),
    )
    body_race_id: Mapped[int] = mapped_column(ForeignKey("body_races.id"))
    body_organ_id: Mapped[int] = mapped_column(ForeignKey("body_organs.id"))
    quantity_organs: Mapped[int] = mapped_column(SMALLINT)
