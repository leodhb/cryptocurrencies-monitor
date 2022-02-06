from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from collector.coinmarketcap import get_cryptocurrencies
from core.config import Settings
from functools import lru_cache

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@lru_cache()
def get_settings():
    return Settings()


@router.get("/", response_class=HTMLResponse)
async def root(request: Request, settings: Settings = Depends(get_settings)):
    items = get_cryptocurrencies({
        "URL": settings.coinmarketcap_apiurl,
        "APIKEY": settings.coinmarketcap_apikey
    })
    return templates.TemplateResponse('index.html', {'request': request, 'coins': items["data"]})