from pip import main
from uvicorn import run
from settings import settings

if __name__ == "__main__":
    run(
        settings.APP,
        host=settings.HOST,
        port=settings.PORT,
        debug=settings.DEBUG,
        reload=settings.DEBUG,
        workers=None if settings.DEBUG else 5
        )