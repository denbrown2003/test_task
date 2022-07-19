import asyncio
from worker.services.price import PriceGenerator



if __name__ == "__main__":
    app = PriceGenerator()
    asyncio.run(app.start())
