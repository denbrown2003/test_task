from time import time
from typing import Dict, List
import aioredis
import orjson
from settings import Settings, settings as base_settings

from . import Idbdriver


class RedisClient(Idbdriver):

    def __init__(self, settings: Settings = base_settings) -> None:
        self.settings = settings
        self._con = aioredis.from_url(
            settings.REDIS,
            encoding="utf-8",
            decode_responses=True
        )

    async def add_tick(self, key:str, data: Dict) -> None:
        score = int(time())
        payload = orjson.dumps(data)
        await self._con.zadd(key, {payload: score})

    async def get_ticks(self, key:str, limit:int) -> List[Dict]:
        data = await self._con.zrange(key, -limit, -1)
        return list(map(lambda x: orjson.loads(x), data))


connects: Dict[str, RedisClient] = {}


def create_connect(name, settings: Settings = base_settings):
    connects[name] = RedisClient(settings)


def get_connection(name: str = "default") -> Idbdriver:
    if not name in connects:
        create_connect(name)
    return connects[name]
