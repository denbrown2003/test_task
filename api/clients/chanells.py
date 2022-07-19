import asyncio
from webbrowser import get
import async_timeout
from fastapi import WebSocket
import orjson

from clients.redis import RedisClient, get_connection


class ChannelListener:

    def __init__(
        self, 
        ws: WebSocket, 
        *, 
        redis: RedisClient = get_connection()
    ) -> None:
        self.stream = ws
        self.redis = redis

    async def listen_channel(self, channel_name: str):
        channel = await self.redis.subscribe([channel_name])
        while True:
            try:
                async with async_timeout.timeout(5):
                    message = await channel.get_message(ignore_subscribe_messages=True)
                    if message:
                        await self.stream.send_json(orjson.loads(message["data"]))
                await asyncio.sleep(1)
            except (orjson.JSONEncodeError, orjson.JSONDecodeError) as e:
                continue

            except asyncio.TimeoutError:
                continue

            except Exception:
                await channel.unsubscribe()
                raise
