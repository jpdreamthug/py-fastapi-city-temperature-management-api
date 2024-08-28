from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import SessionLocal


async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
