from sqlalchemy import ForeignKey, UniqueConstraint, SMALLINT
from sqlalchemy.orm import Mapped, mapped_column

from game import IdIntPkMixin
from game.general.base import Base


class BodyRaceBodyEnergyAssociation(Base, IdIntPkMixin):
    __tablename__ = "body_race_body_energy_association"
    __table_args__ = (
        UniqueConstraint(
            "body_race_id",
            "body_energy_id",
            name="idx_unique_body_race_body_energy",
        ),
    )
    body_race_id: Mapped[int] = mapped_column(ForeignKey("body_races.id"))
    body_energy_id: Mapped[int] = mapped_column(ForeignKey("body_energys.id"))
    quantity_body_energy: Mapped[int] = mapped_column(SMALLINT)
