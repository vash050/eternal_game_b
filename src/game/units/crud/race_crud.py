from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from game.units.models import Race
from game.units.schemas.race import RaceCreate, RaceUpdate


async def get_races(
    session: AsyncSession,
) -> list[Race]:
    stmt = select(Race).order_by(Race.id)
    result: Result = await session.execute(stmt)
    races = result.scalars().all()
    return list(races)


async def get_race(
    session: AsyncSession,
    race_id: int,
) -> Race | None:
    return await session.get(Race, race_id)


async def create_race(
    session: AsyncSession,
    race_in: RaceCreate,
) -> Race:
    race = Race(**race_in.model_dump())
    session.add(race)
    await session.commit()
    return race


async def update_race(
    session: AsyncSession,
    race: Race,
    race_update: RaceUpdate,
) -> Race:
    for name, value in race_update.model_dump().items():
        setattr(race, name, value)
    await session.commit()
    return race


async def delete_race(
    session: AsyncSession,
    race: Race,
) -> None:
    await session.delete(race)
    await session.commit()
