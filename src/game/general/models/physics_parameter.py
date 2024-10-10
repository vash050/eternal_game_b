from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from game import Base, IdIntPkMixin


class PhysicsParameter(Base, IdIntPkMixin):
    name: Mapped[str]
    description: Mapped[str]
    grade: Mapped[int] = mapped_column(ForeignKey("grades.id"))
    is_visibility: Mapped[bool] = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=False)
    category: Mapped[int] = mapped_column(ForeignKey("power_currents.id"))
