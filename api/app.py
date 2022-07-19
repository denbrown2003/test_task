from fastapi import FastAPI, WebSocket
from clients.redis import create_connect

from clients.storage import Storage
from clients.chanells import ChannelListener


app = FastAPI(title="Prices Generator")

@app.websocket("/ticker/{name}/ws")
async def websocket_endpoint(websocket: WebSocket, name: str):
    await websocket.accept()
    channel_name = f"channel:{name}"
    listener = ChannelListener(websocket)
    try:
      await listener.listen_channel(channel_name)
    except Exception as e:
        ...

    await websocket.close()


@app.get("/tickers")
async def get_tickers():
    storage = Storage()
    tickers = await storage.get_active_tickers()
    return tickers
    


@app.get("/healthcheck")
async def check():
    return {
        "status": 1
    }

@app.on_event("startup")
async def startup():
    create_connect("default")
