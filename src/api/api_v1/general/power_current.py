from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.units.get_by_id import power_current_by_id
from core.config import settings
from core.models import db_helper
from game import PowerCurrent as PowerCurrentModel
from game.general.crud.crud import (
    get_objects,
    create_object,
    delete_object,
    update_object,
)
from game.general.schemas.grade import (
    GradeUpdate,
    Grade,
    GradeUpdatePartial,
)
from game.general.schemas.power_current import (
    PowerCurrent,
    PowerCurrentCreate,
    PowerCurrentUpdate,
    PowerCurrentUpdatePartial,
)

router = APIRouter(
    prefix=settings.api_prefix.v1.power_current,
)


@router.get("/power_currents", response_model=list[PowerCurrent])
async def get_power_currents(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await get_objects(session=session, class_object=PowerCurrentModel)


@router.post(
    "/create_power_current",
    response_model=PowerCurrent,
    status_code=status.HTTP_201_CREATED,
)
async def create_power_current(
    power_current_in: PowerCurrentCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await create_object(
        session=session, object_in=power_current_in, class_object=PowerCurrentModel
    )


@router.get("/{power_current_id}/", response_model=PowerCurrent)
async def get_power_current(
    power_current=Depends(power_current_by_id),
):
    return power_current


@router.put("/{power_current_id}/", response_model=PowerCurrent)
async def update_power_current(
    power_current_update: PowerCurrentUpdate,
    power_current=Depends(power_current_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await update_object(
        session=session,
        class_object=power_current,
        object_update=power_current_update,
    )


@router.patch("/{power_current_id}/")
async def update_power_current_partial(
    power_current_update: PowerCurrentUpdatePartial,
    power_current: Grade = Depends(power_current_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await update_object(
        session=session,
        class_object=power_current,
        object_update=power_current_update,
        partial=True,
    )


@router.delete("/{power_current_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_power_current(
    power_current=Depends(power_current_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    await delete_object(session=session, class_object=power_current)
