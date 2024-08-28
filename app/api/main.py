from fastapi import APIRouter

from app.api.routes import city

api_router = APIRouter()
api_router.include_router(city.router, prefix="/cities", tags=["cities"])
