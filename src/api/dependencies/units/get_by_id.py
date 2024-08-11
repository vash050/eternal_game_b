from pathlib import Path
from typing import Annotated

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from game import Grade

from game.general.crud.crud import get_object
from game.units.models import Race


async def race_by_id(
    race_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Race:
    race = await get_object(session=session, object_id=race_id, class_object=Race)
    if race is not None:
        return race
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Race {race_id} not found",
    )


async def grade_by_id(
    grade_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Grade:
    grade = await get_object(session=session, object_id=grade_id, class_object=Grade)
    if grade is not None:
        return grade
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Grade {grade_id} not found",
    )
