import asyncio
from services.price import PriceGenerator
from clients.redis import create_connect


if __name__ == "__main__":
    create_connect("default")
    app = PriceGenerator()
    print("Run Price generator", flush=True)
    asyncio.run(app.start())
