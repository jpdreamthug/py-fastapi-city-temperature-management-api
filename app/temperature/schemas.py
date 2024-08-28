import datetime

from pydantic import BaseModel, ConfigDict


class TemperatureBase(BaseModel):
    city_id: int
    temperature: float
    date_time: datetime.datetime


class TemperatureCreate(TemperatureBase):
    pass


class Temperature(TemperatureBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
