from fastapi import FastAPI



app = FastAPI(title="Prices Generator")



@app.get("/healthcheck")
async def check():
    return {
        "status": 1
    }
