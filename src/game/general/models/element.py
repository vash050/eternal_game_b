from sqlalchemy import Column, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from game import Base, IdIntPkMixin


class Element(Base, IdIntPkMixin):
    name: Mapped[str]
    description: Mapped[str]
    features = Column(JSONB)
    img_url: Mapped[str]
    grade_id: Mapped[int] = mapped_column(ForeignKey("grades.id"))
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)