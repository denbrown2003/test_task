from typing import List, Optional
from settings import Settings, settings as base_settings
from . import Idbdriver
from . redis import get_connection
from models.ticker import Tick, Ticker


class Storage:

    def __init__(
        self, 
        db_client: Idbdriver = get_connection(),
        settings: Settings = base_settings
    ) -> None:
        self.settings = settings
        self.client = db_client

    async def get_last_tick(self, ticker: str) -> Optional[Tick]:
        tickets = await self.client.get_ticks(ticker, 1)
        if tickets:
            return tickets[0]
    
    async def get_ticker_history(self, ticker: str, limit: int) -> List[Tick]:
        return  await self.client.get_ticks(ticker, limit)

    async def update_ticker(self, ticker: Ticker) -> None:
        await self.client.add_tick(ticker.name, ticker.last_tick.dict())
