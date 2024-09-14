from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.dependencies.units.get_by_id import element_by_id
from core.config import settings
from core.models import db_helper
from game import Element as Elementelement
from game.general.crud.crud import (
    get_objects,
    create_object,
    delete_object,
    update_object,
)
from game.general.schemas.element import (
    ElementUpdate,
    Element,
    ElementCreate,
    ElementUpdatePartial,
)

router = APIRouter(prefix=settings.api_prefix.v1.element)


@router.get("/elements", response_model=list[Element])
async def get_elements(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await get_objects(session=session, class_object=ElementModel)


@router.post(
    "/create-element",
    response_model=Element,
    status_code=status.HTTP_201_CREATED,
)
async def create_element(
    element_in: ElementCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await create_object(
        session=session, object_in=element_in, class_object=ElementModel
    )


@router.get("/{element_id}/", response_model=Element)
async def get_element(
    element=Depends(element_by_id),
):
    return element


@router.put("/{element_id}/", response_model=Element)
async def update_element(
    element_update: ElementUpdate,
    element=Depends(element_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await update_object(
        session=session,
        class_object=element,
        object_update=element_update,
    )


@router.patch("/{element_id}/")
async def update_element_partial(
    element_update: ElementUpdatePartial,
    element: Element = Depends(element_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await update_object(
        session=session,
        class_object=element,
        object_update=element_update,
        partial=True,
    )


@router.delete("/{element_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_element(
    element=Depends(element_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    await delete_object(session=session, class_object=element)
