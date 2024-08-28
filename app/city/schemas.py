from app.core.db import Base


class CityBase(Base):
    name: str
    additional_info: str


class CityCreate(CityBase):
    pass


class City(CityBase):
    id: int

    class Config:
        orm_mode = True
