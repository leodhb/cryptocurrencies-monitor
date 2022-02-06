from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from collector.coinmarketcap import get_cryptocurrencies
from functools import lru_cache
from config import Settings

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@lru_cache()
def get_settings():
    return Settings()

@app.get("/")
async def root(settings: Settings = Depends(get_settings)):
    return get_cryptocurrencies(
        {
            "URL": settings.coinmarketcap_apiurl,
            "APIKEY": settings.coinmarketcap_apikey
        }
    )


