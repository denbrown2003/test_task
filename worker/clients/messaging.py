from models.ticker import Ticker
from . import Ipublisher
from .redis import RedisClient, get_connection
import orjson


class RedisPublisher(Ipublisher):

    def __init__(self, client: RedisClient = get_connection()) -> None:
        self.client = client

    async def publish_ticker(self, ticker: Ticker) -> None:
        data = orjson.dumps(
            {"price": ticker.last_tick.price, "timestamp": int(ticker.last_tick.timestamp)}
        )
        route = f"channel:{ticker.name}"
        await self.client.publish_message(route, data)
