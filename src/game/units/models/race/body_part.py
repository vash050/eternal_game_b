from sqlalchemy.orm import Mapped

from game import IdIntPkMixin
from game.general.base import Base


class BodyPart(Base, IdIntPkMixin):
    name: Mapped[str]
    description: Mapped[str]
    quantity_slots: Mapped[int]
    size_slots: Mapped[int]
