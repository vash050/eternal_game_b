from sqlalchemy.orm import Mapped

from game import IdIntPkMixin
from game.general.base import Base


class BodyCharacteristic(Base, IdIntPkMixin):
    name: Mapped[str]
    description: Mapped[str]
