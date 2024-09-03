from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.units.get_by_id import unit_level_by_id
from core.config import settings
from core.models import db_helper
from game.general.crud.crud import (
    get_objects,
    create_object,
    delete_object,
    update_object,
)

from game.units.schemas.unit_level import (
    UnitLevel,
    UnitLevelCreate,
    UnitLevelUpdate,
    UnitLevelUpdatePartial,
)
from game import UnitLevel as UnitLevelModel

router = APIRouter(
    prefix=settings.api_prefix.v1.unit_level,
)


@router.get("/unit-levels", response_model=list[UnitLevel])
async def get_unit_levels(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await get_objects(session=session, class_object=UnitLevelModel)


@router.post(
    "/create-unit-level",
    response_model=UnitLevel,
    status_code=status.HTTP_201_CREATED,
)
async def create_unit_level(
    unit_level_in: UnitLevelCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await create_object(
        session=session, object_in=unit_level_in, class_object=UnitLevelModel
    )


@router.get("/{unit-level-id}/", response_model=UnitLevel)
async def get_unit_level(
    unit_level=Depends(unit_level_by_id),
):
    return unit_level


@router.put("/{unit-level-id}/", response_model=UnitLevel)
async def update_unit_level(
    unit_level_update: UnitLevelUpdate,
    unit_level=Depends(unit_level_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await update_object(
        session=session,
        class_object=unit_level,
        object_update=unit_level_update,
    )


@router.patch("/{unit-level-id}/")
async def update_unit_level_partial(
    unit_level_update: UnitLevelUpdatePartial,
    unit_level: UnitLevel = Depends(unit_level_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await update_object(
        session=session,
        class_object=unit_level,
        object_update=unit_level_update,
        partial=True,
    )


@router.delete("/{unit-level-id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_unit_level(
    unit_level=Depends(unit_level_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    await delete_object(session=session, class_object=unit_level)
