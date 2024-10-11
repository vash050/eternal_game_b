from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.units.get_by_id import physics_parameter_by_id
from core.config import settings
from core.models import db_helper
from game import PhysicsParameter as PhysicsParameterModel
from game.general.crud.crud import (
    get_objects,
    create_object,
    delete_object,
    update_object,
)

from game.general.schemas.physics_parameter import (
    PhysicsParameter,
    PhysicsParameterCreate,
    PhysicsParameterUpdate,
    PhysicsParameterUpdatePartial,
)

router = APIRouter(
    prefix=settings.api_prefix.v1.physics_parameter,
)


@router.get("/physics_parameters", response_model=list[PhysicsParameter])
async def get_physics_parameters(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await get_objects(session=session, class_object=PhysicsParameterModel)


@router.post(
    "/create_physics_parameter",
    response_model=PhysicsParameter,
    status_code=status.HTTP_201_CREATED,
)
async def create_physics_parameter(
    physics_parameter_in: PhysicsParameterCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await create_object(
        session=session,
        object_in=physics_parameter_in,
        class_object=PhysicsParameterModel,
    )


@router.get("/{physics_parameter_id}/", response_model=PhysicsParameter)
async def get_physics_parameter(
    physics_parameter=Depends(physics_parameter_by_id),
):
    return physics_parameter


@router.put("/{physics_parameter_id}/", response_model=PhysicsParameter)
async def update_physics_parameter(
    physics_parameter_update: PhysicsParameterUpdate,
    physics_parameter=Depends(physics_parameter_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await update_object(
        session=session,
        class_object=physics_parameter,
        object_update=physics_parameter_update,
    )


@router.patch("/{physics_parameter_id}/")
async def update_physics_parameter_partial(
    physics_parameter_update: PhysicsParameterUpdatePartial,
    physics_parameter: PhysicsParameter = Depends(physics_parameter_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await update_object(
        session=session,
        class_object=physics_parameter,
        object_update=physics_parameter_update,
        partial=True,
    )


@router.delete("/{physics_parameter_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_physics_parameter(
    physics_parameter=Depends(physics_parameter_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    await delete_object(session=session, class_object=physics_parameter)
