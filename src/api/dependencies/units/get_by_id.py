from pathlib import Path
from typing import Annotated

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from game.units.crud import race_crud
from game.units.models import Race


async def race_by_id(
    race_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Race:
    race = await race_crud.get_race(session=session, race_id=race_id)
    if race is not None:
        return race
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Race {race_id} not found",
    )
