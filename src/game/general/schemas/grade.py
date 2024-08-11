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


class Grade(GradeBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
