from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.units.get_by_id import race_by_id
from core.models import db_helper
from game.general.crud.crud import (
    get_objects,
    create_object,
    delete_object,
    update_object,
)

from game.units.schemas.race import Race, RaceCreate, RaceUpdate, RaceUpdatePartial
from game import Race as RaceModel

router = APIRouter()


@router.get("/races", response_model=list[Race])
async def get_races(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await get_objects(session=session, class_object=RaceModel)


@router.post(
    "/create-race",
    response_model=Race,
    status_code=status.HTTP_201_CREATED,
)
async def create_race(
    race_in: RaceCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await create_object(
        session=session, object_in=race_in, class_object=RaceModel
    )


@router.get("/{race_id}/", response_model=Race)
async def get_race(
    race=Depends(race_by_id),
):
    return race


@router.put("/{race_id}/", response_model=Race)
async def update_race(
    race_update: RaceUpdate,
    race=Depends(race_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await update_object(
        session=session,
        class_object=race,
        object_update=race_update,
    )


@router.patch("/{race_id}/")
async def update_race_partial(
    race_update: RaceUpdatePartial,
    race: Race = Depends(race_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await update_object(
        session=session,
        class_object=race,
        object_update=race_update,
        partial=True,
    )


@router.delete("/{race_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_race(
    race=Depends(race_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    await delete_object(session=session, class_object=race)
