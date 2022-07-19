from time import time
from numbers import Number
from pydantic import BaseModel


class Tick(BaseModel):
    price: Number = 0
    timestamp: int = int(time())

    class Config:
        arbitrary_types_allowed = True


class Ticker(BaseModel):
    id: int
    name: str
    last_tick: Tick
