from typing import Tuple
from pydantic import BaseSettings, RedisDsn


class Settings(BaseSettings):
    CHANGE_DELAY: int = 1 # delay in seconds
    DEBUG: bool = True
    REDIS: RedisDsn = "redis://localhost"
    TICKER_NAME_PREFIX: str = "ticker"
    TICKER_RANGE: Tuple[int, int] = (0, 1)


settings = Settings()
