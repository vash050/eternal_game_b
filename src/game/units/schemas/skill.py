from pydantic import BaseModel, ConfigDict
from .unit import Unit


class SkillBase(BaseModel):
    name: str
    description: str
    img_url: str | None
    skill_bonus: dict[str, float] | None
    # магия, физика и т.д.
    units: list["Unit"]
    is_active: bool


class SkillCreate(SkillBase):
    pass


class SkillUpdate(SkillBase):
    pass


class SkillUpdatePartial(SkillCreate):
    name: str | None
    description: str | None
    img_url: str | None
    skill_bonus: dict[str, float] | None
    is_active: bool | None
    # main_parameters: list["MainParameters"] | None
    unit: "Unit" | None
    # hidden_parameters: list["HiddenParameters"] | None


class Skill(SkillBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
