from pathlib import Path
from typing import Annotated

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from game import Grade, PowerCurrent, Element
from game.general.crud.crud import get_object
from game.units.models import Race, UnitLevel


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


async def power_current_by_id(
        power_current_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> PowerCurrent:
    power_current = await get_object(
        session=session, object_id=power_current_id, class_object=PowerCurrent
    )
    if power_current is not None:
        return power_current
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Grade {power_current_id} not found",
    )


async def unit_level_by_id(
        unit_level_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> UnitLevel:
    unit_level = await get_object(
        session=session, object_id=unit_level_id, class_object=UnitLevel
    )
    if unit_level is not None:
        return unit_level
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Grade {unit_level_id} not found",
    )


async def element_by_id(
        element_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Element:
    element = await get_object(
        session=session, object_id=element_id, class_object=Element
    )
    if element is not None:
        return element
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Element {element_id} not found",
    )