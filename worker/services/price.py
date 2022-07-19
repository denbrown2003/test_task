import asyncio
from random import random, randint
from time import time
from typing import List

from settings import Settings, settings as base_configs
from models.ticker import Tick, Ticker
from clients.storage import Storage
from clients import Ipublisher, messaging


# Price changer from task description
def generate_movement(price: int):
    movement = -1 if random() < 0.5 else 1
    return price + movement
# ------------------


class PriceGenerator:

    def __init__(
        self, 
        storage: Storage = Storage(),
        messager: Ipublisher = messaging.RedisPublisher(),
        settings: Settings = base_configs
        ) -> None:
        self.settings = settings
        self.storage = storage
        self.messager = messager

        self.ticker_range = settings.TICKER_RANGE
        self.ticker_prefix = settings.TICKER_NAME_PREFIX

        self.tickers: List[Ticker] = []

    async def load_tickers(self):
        for id_ in range(*self.ticker_range):
            last_tick = await self.storage.get_last_tick(f"{self.ticker_prefix}_{id_}") or Tick(price=randint(200, 1000))
            self.tickers.append(
                Ticker(
                    id=id_,
                    name=f"{self.ticker_prefix}_{id_}",
                    last_tick=last_tick
                    )
            )
        await self.storage.save_active_ticker(self.tickers)

    async def worker(self):
        for ticker in self.tickers:
            new_price = generate_movement(ticker.last_tick.price)
            ticker.last_tick.price = new_price if new_price else 0
            ticker.last_tick.timestamp = time()

            await self.storage.update_ticker(ticker)
            await self.messager.publish_ticker(ticker)

    async def start(self):
        await self.load_tickers()

        while True:
            await asyncio.sleep(self.settings.CHANGE_DELAY)
            await self.worker()
