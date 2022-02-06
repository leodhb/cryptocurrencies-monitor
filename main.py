from fastapi import FastAPI, Depends, Request
from fastapi.staticfiles import StaticFiles
from api.main_router import router as main_rotuer

def include_routers(app):
    app.include_router(main_rotuer)

def configure_static_files(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")

def start_application():
    app = FastAPI()
    include_routers(app)
    configure_static_files(app)
    return app

app = start_application()








