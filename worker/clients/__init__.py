import abc
from typing import List, Dict
from models.ticker import Ticker


class Idbdriver(abc.ABC):
    
    @abc.abstractmethod
    async def add_tick(self, key:str, data: dict):
        ...

    @abc.abstractmethod
    async def get_ticks(self, key:str, limit:int) -> List[Dict]:
        ...


class Ipublisher(abc.ABC):
    
    @abc.abstractmethod
    async def publish_ticker(ticker: Ticker) -> None:
        ...