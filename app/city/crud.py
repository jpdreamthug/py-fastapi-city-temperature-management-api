from typing import Sequence

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import models
from app.city import schemas


async def get_all_cities(db: AsyncSession) -> Sequence[models.City]:
    query = select(models.City)
    cities_list = await db.execute(query)
    return cities_list.scalars().all()


async def create_city(db: AsyncSession, city: schemas.CityCreate) -> models.City:
    new_city = models.City(
        name=city.name,
        additional_info=city.additional_info
    )
    db.add(new_city)
    try:
        await db.commit()
        await db.refresh(new_city)
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=400, detail="City with this name already exists"
        )
    return new_city
