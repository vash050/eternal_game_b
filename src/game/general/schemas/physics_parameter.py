from pydantic import BaseModel, ConfigDict


class PhysicsParameterBase(BaseModel):
    name: str
    description: str
    grade: int
    is_visibility: bool
    is_active: bool
    category: int


class PhysicsParameterCreate(PhysicsParameterBase):
    pass


class PhysicsParameterUpdate(PhysicsParameterBase):
    pass


class PhysicsParameterUpdatePartial(PhysicsParameterCreate):
    name: str | None = None
    description: str | None = None
    grade: int | None = None
    is_visibility: bool | None = None
    is_active: bool | None = None
    category: int | None = None


class PhysicsParameter(PhysicsParameterBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
