from fastapi import FastAPI
from app.app.api.endpoints import login
from app.app.db.init_db import init_db
from app.app.api.endpoints import otplogin

app = FastAPI()

init_db()
app.include_router(login.router)
app.include_router(otplogin.router)

