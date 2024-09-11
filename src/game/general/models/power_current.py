from sqlalchemy import Boolean
from sqlalchemy.orm import Mapped, mapped_column

from game import Base, IdIntPkMixin


# TODO: переименовать в ParameterCategory
class PowerCurrent(Base, IdIntPkMixin):
    name: Mapped[str]
    description: Mapped[str]
    color: Mapped[str]
    img_url: Mapped[str]
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)
