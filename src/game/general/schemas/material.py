from pydantic import BaseModel, ConfigDict


class MaterialBase(BaseModel):

    name: str
    description: str
    # element_details: list
    endurance: int
    features: dict[str, str]
    img_url: str
    grade_id: int
    is_active: bool


class MaterialCreate(MaterialBase):
    pass


class MaterialUpdate(MaterialBase):
    pass


class MaterialUpdatePartial(MaterialBase):
    name: str | None = None
    description: str | None = None
    endurance: int | None = None
    features: dict[str, str] | None = None
    img_url: str | None = None
    grade_id: int | None = None
    is_active: bool | None = False


class Material(MaterialBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
