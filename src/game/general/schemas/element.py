from pydantic import BaseModel, ConfigDict


class ElementBase(BaseModel):
    name: str
    description: str
    features: dict[str, str]
    img_url: str
    grade_id: int
    is_active: bool


class ElementCreate(ElementBase):
    pass


class ElementUpdate(ElementBase):
    pass


class ElementUpdatePartial(ElementBase):
    name: str | None = None
    description: str | None = None
    features: dict[str, str] | None = None
    img_url: str | None = None
    grade_id: int | None = None
    is_active: bool | None = False


class Element(ElementBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
