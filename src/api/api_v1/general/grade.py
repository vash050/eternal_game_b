from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.units.get_by_id import grade_by_id
from core.config import settings
from core.models import db_helper
from game import Grade as GradeModel
from game.general.crud.crud import (
    get_objects,
    create_object,
    delete_object,
    update_object,
)
from game.general.schemas.grade import (
    GradeUpdate,
    Grade,
    GradeCreate,
    GradeUpdatePartial,
)

router = APIRouter(
    prefix=settings.api_prefix.v1.grade,
)


@router.get("/grades", response_model=list[Grade])
async def get_grades(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await get_objects(session=session, class_object=GradeModel)


@router.post(
    "/create-grade",
    response_model=Grade,
    status_code=status.HTTP_201_CREATED,
)
async def create_grade(
    grade_in: GradeCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await create_object(
        session=session, object_in=grade_in, class_object=GradeModel
    )


@router.get("/{grade_id}/", response_model=Grade)
async def get_grade(
    grade=Depends(grade_by_id),
):
    return grade


@router.put("/{grade_id}/", response_model=Grade)
async def update_race(
    grade_update: GradeUpdate,
    grade=Depends(grade_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await update_object(
        session=session,
        class_object=grade,
        object_update=grade_update,
    )


@router.patch("/{grade_id}/")
async def update_grade_partial(
    grade_update: GradeUpdatePartial,
    grade: Grade = Depends(grade_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await update_object(
        session=session,
        class_object=grade,
        object_update=grade_update,
        partial=True,
    )


@router.delete("/{grade_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_grade(
    grade=Depends(grade_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    await delete_object(session=session, class_object=grade)
