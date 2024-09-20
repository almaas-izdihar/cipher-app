from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.routes import router

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/gui"), name="gui")
app.include_router(router)
