from fastapi import FastAPI
from app.app.api.endpoints import login

app = FastAPI()

app.include_router(login.router)