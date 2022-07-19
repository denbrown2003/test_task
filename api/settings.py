from pydantic import BaseSettings, RedisDsn


class Settings(BaseSettings):
    APP: str = "app:app"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True

    REDIS: RedisDsn = "redis://localhost"

settings = Settings()
