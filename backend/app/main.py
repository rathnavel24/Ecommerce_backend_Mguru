from fastapi import FastAPI
from app.app.api.endpoints import login
from app.app.api.endpoints import signup
from app.app.db.init_db import init_db

app = FastAPI()

#init_db()

app.include_router(signup.router)
app.include_router(login.router)