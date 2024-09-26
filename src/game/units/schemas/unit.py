from pydantic import BaseModel, ConfigDict
from .race import Race
from .unit_level import UnitLevel
from .skill import Skill


class UnitBase(BaseModel):
    name: str
    description: str
    img_url: str | None
    race: list["Race"]
    unit_level: list["UnitLevel"]
    protection: dict[str, int]
    damage: dict[str, int]
    penetrate: dict[str, int]
    speed_battle: float
    speed_travel: float
    is_active: bool
    # main_parameters: list["MainParameters"]
    skills: list["Skill"]
    # hidden_parameters: list["HiddenParameters"]


class UnitCreate(UnitBase):
    pass


class UnitUpdate(UnitBase):
    pass


class UnitUpdatePartial(UnitCreate):
    name: str | None
    description: str | None
    img_url: str | None
    race: list["Race"] | None
    unit_level: list["UnitLevel"] | None
    protection: dict[str, int] | None
    damage: dict[str, int] | None
    penetrate: dict[str, int] | None
    speed_battle: float | None
    speed_travel: float | None
    is_active: bool | None
    # main_parameters: list["MainParameters"] | None
    skills: list["Skill"] | None
    # hidden_parameters: list["HiddenParameters"] | None

class Unit(UnitBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
