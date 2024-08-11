from pydantic import BaseModel, ConfigDict


class GradeBase(BaseModel):
    name: str
    description: str
    color: str
    race_bonus: dict[str, str]
    img_url: str
    is_active: bool


class GradeCreate(GradeBase):
    pass


class GradeUpdate(GradeBase):
    pass


class GradeUpdatePartial(GradeCreate):
    name: str | None = None
    description: str | None = None
    color: str | None = None
    race_bonus: dict[str, str] | None = None
    img_url: str | None = None
    is_active: bool | None = False


class Grade(GradeBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
