from typing import Dict, List
import time

import orjson
import aioredis

from settings import Settings, settings as base_settings


class RedisClient:

    def __init__(self, settings: Settings = base_settings) -> None:
        self.settings = settings
        self._con = aioredis.from_url(
            settings.REDIS,
            encoding="utf-8",
            decode_responses=True
        )

    async def set(self, key: str, data: Dict):
        await self._con.set(key, orjson.dumps(data))
    
    async def get(self, key: str) -> Dict:
        return orjson.loads(await self._con.get(key))

    async def add_tick(self, key: str, data: Dict) -> None:
        score = int(time.time())
        payload = orjson.dumps(data)
        await self._con.zadd(key, {payload: score})

    async def get_ticks(self, key: str, limit: int = None) -> List[Dict]:
        if limit is None:
            data = await self._con.zrangebyscore(key, "-inf", "+inf")
        else:
            data = await self._con.zrange(key, -limit, -1)
        return list(map(lambda x: orjson.loads(x), data))

    async def subscribe(self, routes: List[str]):
        pubsub = self._con.pubsub()
        await pubsub.subscribe(*routes)
        return pubsub

connects: Dict[str, RedisClient] = {}


def create_connect(name, settings: Settings = base_settings):
    connects[name] = RedisClient(settings)


def get_connection(name: str = "default") -> RedisClient:
    if not name in connects:
        create_connect(name)
    return connects[name]
