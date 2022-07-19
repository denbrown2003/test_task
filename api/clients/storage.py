from typing import Dict
from settings import Settings, settings as base_settings
from . redis import get_connection, RedisClient


class Storage:

    def __init__(self, db_client: RedisClient = get_connection()) -> None:
        self.client = db_client

    async def get_active_tickers(self) -> Dict:
        tickers = await self.client.get("active_tickers")
        return tickers
