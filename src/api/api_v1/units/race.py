from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.units.get_by_id import race_by_id
from core.config import settings
from core.models import db_helper
from units.crud import race_crud
from units.schemas.race import Race, RaceCreate, RaceUpdate

router = APIRouter()


@router.get("/races", response_model=list[Race])
async def get_races(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await race_crud.get_races(session=session)


@router.post(
    "/create-race",
    response_model=Race,
    status_code=status.HTTP_201_CREATED,
)
async def create_race(
    race_in: RaceCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await race_crud.create_race(session=session, race_in=race_in)


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
    return await race_crud.update_race(
        session=session,
        race=race,
        race_update=race_update,
    )


@router.delete("/{race_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_race(
    race=Depends(race_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    await race_crud.delete_race(session=session, race=race)
