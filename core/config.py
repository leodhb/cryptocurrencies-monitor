from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Crypto Tracker"
    version: str = "1.0.0"
    coinmarketcap_apiurl: str
    coinmarketcap_apikey: str

    class Config():
        env_file = ".env"