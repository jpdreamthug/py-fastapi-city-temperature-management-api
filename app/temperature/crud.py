from fastapi import HTTPException
from sqlalchemy import select, Sequence
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import models
from app.temperature import schemas


async def get_temperatures(db: AsyncSession) -> Sequence[models.Temperature]:
    query = select(models.Temperature)
    temperatures_list = await db.execute(query)
    return temperatures_list.scalars().all()


async def get_temperature_by_city_id(
        db: AsyncSession, city_id: int
) -> Sequence[models.Temperature]:
    query = select(models.Temperature).where(models.Temperature.city_id == city_id)
    result = await db.execute(query)
    return result.scalars().all()
