from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from game import IdIntPkMixin
from game.general.base import Base


if TYPE_CHECKING:
    from game.units.models.body_part import BodyPart
    from game.units.models.body_organ import BodyOrgan
    from game.units.models.race.body_possible_state import BodyPossibleState
    from game.units.models.body_characteristic import BodyCharacteristic
    from game.units.models.race.body_energy import BodyEnergy


class BodyRace(Base, IdIntPkMixin):
    quantity_parts_all: Mapped[int]
    list_parts: Mapped[list["BodyPart"]] = relationship(
        back_populates="body_races",
        secondary="body_race_body_part_association",
    )
    quantity_organs_all: Mapped[int]
    list_organs: Mapped[list["BodyOrgan"]] = relationship(
        back_populates="body_races",
        secondary="body_race_body_organ_association",
    )
    list_possible_states: Mapped[list["BodyPossibleState"]] = relationship(
        back_populates="body_races",
        secondary="body_race_body_possible_state_association",
    )
    list_characteristic: Mapped[list["BodyCharacteristic"]] = relationship(
        back_populates="body_races",
        secondary="body_race_body_characteristic_association",
    )
    list_energies: Mapped[list["BodyEnergy"]] = relationship(
        back_populates="body_races",
        secondary="body_race_body_energy_association",
    )
