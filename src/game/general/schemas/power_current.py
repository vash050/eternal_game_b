from pydantic import BaseModel, ConfigDict


class PowerCurrentBase(BaseModel):
    name: str
    description: str
    color: str
    img_url: str
    is_active: bool


class PowerCurrentCreate(PowerCurrentBase):
    pass


class PowerCurrentUpdate(PowerCurrentBase):
    pass


class PowerCurrentUpdatePartial(PowerCurrentCreate):
    name: str | None = None
    description: str | None = None
    color: str | None = None
    img_url: str | None = None
    is_active: bool | None = False


class PowerCurrent(PowerCurrentBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
