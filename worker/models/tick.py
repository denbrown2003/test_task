from datetime import datetime
from numbers import Number
from pydantic import BaseModel


class Tick(BaseModel):
    ticker: str
    price: Number
    timestamp: datetime
