from pydantic import BaseModel, ConfigDict


class UnitLevelBase(BaseModel):
    name: int
    description: str
    bonus: dict[str, str]
    max_experience: int
    is_active: bool


class UnitLevelCreate(UnitLevelBase):
    pass


class UnitLevelUpdate(UnitLevelBase):
    pass


class UnitLevelUpdatePartial(UnitLevelCreate):
    name: str | None = None
    description: str | None = None
    race_bonus: dict[str, str] | None = None
    bonus: int = None
    is_active: bool | None = False


class UnitLevel(UnitLevelBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
