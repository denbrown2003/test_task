import aioredis

from settings import Settings, settings as base_settings

from . import Idbdriver


class Redis(Idbdriver):

    def __init__(self, settings: Settings = base_settings) -> None:
        self.settings = settings

    async def add_item(self, key:str, price: dict):
        ...


def get_connection(name: str = "default") -> Idbdriver:
    return Redis()
