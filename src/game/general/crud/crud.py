from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload


async def get_objects(
        session: AsyncSession,
        class_object: object,
) -> list[object]:
    stmt = select(class_object).order_by(class_object.id)
    result: Result = await session.execute(stmt)
    objects = result.scalars().all()
    return list(objects)


async def get_objects_m2m(
        session: AsyncSession,
        class_object: object,
        field_name: object,
) -> list[object]:
    stmt = (
        select(class_object)
        .options(
            selectinload(field_name)
        )
        .order_by(class_object.id)
    )
    result = await session.execute(stmt)
    objects = result.scalars().all()
    return list(objects)


async def get_object(
        session: AsyncSession,
        object_id: int,
        class_object: object,
) -> object | None:
    return await session.get(class_object, object_id)


async def create_object(
        session: AsyncSession,
        object_in: object,
        class_object: object,
) -> object:
    result_object = class_object(**object_in.model_dump())
    session.add(result_object)
    await session.commit()
    return result_object


async def update_object(
        session: AsyncSession,
        class_object: object,
        object_update: object,
        partial: bool = False,
) -> object:
    for name, value in object_update.model_dump(exclude_unset=partial).items():
        setattr(class_object, name, value)
    await session.commit()
    return class_object


async def delete_object(
        session: AsyncSession,
        class_object: object,
) -> None:
    await session.delete(class_object)
    await session.commit()
