from models.ticker import Ticker
from . import Ipublisher
from .redis import RedisClient, get_connection


class RedisPublisher(Ipublisher):

    def __init__(self, client: RedisClient = get_connection()) -> None:
        self.client = client

    async def publish_message(self, ruote: str, data: bytes) -> None:
        ...

    async def publish_ticker(self, ticker: Ticker) -> None:
        ...