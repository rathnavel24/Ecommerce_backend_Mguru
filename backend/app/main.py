from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.app.api.endpoints import login
from app.app.api.endpoints import signup
from app.app.api.endpoints import getuserinfo
from app.app.db.init_db import init_db

app = FastAPI()

init_db()
app.include_router(login.router)

init_db()
app.include_router(reset_password.router)
#init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(signup.router)
app.include_router(login.router)
app.include_router(getuserinfo.router)
