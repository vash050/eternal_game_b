from pydantic import BaseModel

from game.general.schemas.element import Element


class MaterialBase(BaseModel):
    name: str
    description: str
    endurance: int
    features: dict[str, str]
    img_url: str
    grade_id: int
    is_active: bool
    elements: list["Element"]


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
    id: int
