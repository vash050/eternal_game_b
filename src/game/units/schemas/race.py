from pydantic import BaseModel, ConfigDict


class RaseBase(BaseModel):
    name: str
    description: str
    race_bonus: dict[str, str]
    img_url: str
    is_active: bool


class RaceCreate(RaseBase):
    pass


class RaceUpdate(RaseBase):
    pass


class RaceUpdatePartial(RaceCreate):
    name: str | None = None
    description: str | None = None
    race_bonus: dict[str, str] | None = None
    img_url: str | None = None
    is_active: bool | None = False


class Race(RaseBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
