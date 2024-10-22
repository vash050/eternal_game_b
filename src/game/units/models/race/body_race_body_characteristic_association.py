from sqlalchemy import ForeignKey, UniqueConstraint, SMALLINT
from sqlalchemy.orm import Mapped, mapped_column

from game import IdIntPkMixin
from game.general.base import Base


class BodyRaceBodyCharacteristicAssociation(Base, IdIntPkMixin):
    __tablename__ = "body_race_body_characteristic_association"
    __table_args__ = (
        UniqueConstraint(
            "body_race_id",
            "body_characteristic_id",
            name="idx_unique_body_race_characteristic",
        ),
    )
    body_race_id: Mapped[int] = mapped_column(ForeignKey("body_races.id"))
    body_characteristic_id: Mapped[int] = mapped_column(
        ForeignKey("body_characteristics.id")
    )
    quantity_characteristic: Mapped[int] = mapped_column(SMALLINT)
