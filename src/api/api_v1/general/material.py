from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.units.get_by_id import material_by_id
from core.config import settings
from core.models import db_helper
from game import Material as MaterialModel
from game.general.crud.crud import (
    get_objects,
    create_object,
    delete_object,
    update_object,
    get_objects_m2m,
)
from game.general.schemas.material import (
    MaterialUpdate,
    Material,
    MaterialCreate,
    MaterialUpdatePartial,
)

router = APIRouter(prefix=settings.api_prefix.v1.material)


@router.get("/materials", response_model=list[Material])
async def get_materials(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await get_objects_m2m(
        session=session, class_object=MaterialModel, field_name=MaterialModel.elements
    )


@router.post(
    "/create-material",
    response_model=Material,
    status_code=status.HTTP_201_CREATED,
)
async def create_material(
    material_in: MaterialCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await create_object(
        session=session, object_in=material_in, class_object=MaterialModel
    )


@router.get("/{material_id}/", response_model=Material)
async def get_material(
    material=Depends(material_by_id),
):
    return material


@router.put("/{material_id}/", response_model=Material)
async def update_material(
    material_update: MaterialUpdate,
    material=Depends(material_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await update_object(
        session=session,
        class_object=material,
        object_update=material_update,
    )


@router.patch("/{material_id}/")
async def update_material_partial(
    material_update: MaterialUpdatePartial,
    material: Material = Depends(material_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await update_object(
        session=session,
        class_object=material,
        object_update=material_update,
        partial=True,
    )


@router.delete("/{material_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_material(
    material=Depends(material_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    await delete_object(session=session, class_object=material)
