import asyncio
from random import random

from settings import Settings, settings as base_configs
from models.tick import Tick


# Price changer from task description
def generate_movement():
    movement = -1 if random() < 0.5 else 1
    return movement
# ------------------


class PriceGenerator:

    def __init__(self, settings: Settings = base_configs) -> None:
        self.settings = settings

    async def worker(self):
        ...

    async def start(self):
        while True:
            await asyncio.sleep(self.settings.DELAY)
            await self.worker()
