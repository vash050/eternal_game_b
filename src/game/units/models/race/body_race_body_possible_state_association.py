from sqlalchemy import ForeignKey, UniqueConstraint, SMALLINT
from sqlalchemy.orm import Mapped, mapped_column

from game import IdIntPkMixin
from game.general.base import Base


class BodyRaceBodyPossibleStateAssociation(Base, IdIntPkMixin):
    __tablename__ = "body_race_body_possible_state_association"
    __table_args__ = (
        UniqueConstraint(
            "body_race_id",
            "body_possible_state_id",
            name="idx_unique_body_race_body_possible_state",
        ),
    )
    body_race_id: Mapped[int] = mapped_column(ForeignKey("body_races.id"))
    body_possible_state_id: Mapped[int] = mapped_column(
        ForeignKey("body_possible_states.id")
    )
    quantity_possible_states: Mapped[int] = mapped_column(SMALLINT)
