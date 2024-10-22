from sqlalchemy.orm import Mapped

from game import Base, IdIntPkMixin


class Energy(Base, IdIntPkMixin):
    name: Mapped[str]
    description: Mapped[str]
    color: Mapped[str]
