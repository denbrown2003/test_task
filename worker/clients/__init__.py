import abc
from numbers import Number


class Idbdriver(abc.ABC):
    
    @abc.abstractmethod
    async def add_item(self, key:str, object: dict):
        ...
