from typing import List
from settings import Settings, settings as base_settings
from .redis import Idbdriver, get_connection
from models.tick import Tick


class Storage:

    def __init__(
        self, 
        db_client: Idbdriver = get_connection(),
        settings: Settings = base_settings
    ) -> None:
        self.settings = settings
        self.client = db_client
    
    async def save_tick(self, tick: Tick) -> None:
        ...

    async def get_last_tick(self, ticker: str) -> Tick:
        ...
    
    async def get_ticker_history(self, ticker: str) -> List[Tick]:
        ...
