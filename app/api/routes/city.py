from fastapi import APIRouter, Depends
from sqlalchemy import Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from app.city import schemas, crud
from app.dependencies import get_db


router = APIRouter()


@router.get("/", response_model=list[schemas.City])
async def read_cities(
        db: AsyncSession = Depends(get_db)
) -> Sequence[schemas.City]:
    return await crud.get_all_cities(db=db)


@router.post("/", response_model=schemas.CityCreate)
async def add_city(
    city: schemas.CityCreate,
    db: AsyncSession = Depends(get_db)
) -> schemas.City:
    return await crud.create_city(db=db, city=city)
