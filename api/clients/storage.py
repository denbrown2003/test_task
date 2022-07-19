from typing import Dict, List
from . redis import get_connection, RedisClient


class Storage:

    def __init__(self, db_client: RedisClient = get_connection()) -> None:
        self.client = db_client

    async def get_active_tickers(self) -> Dict:
        tickers = await self.client.get("active_tickers")
        return tickers

    async def get_ticker_history(self, ticker: str, limit: int) -> List[Dict]:
        return await self.client.get_ticks(ticker, limit)
