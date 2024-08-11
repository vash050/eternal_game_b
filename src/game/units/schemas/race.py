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


class Race(RaseBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
