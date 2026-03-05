from fastapi import FastAPI
from app.app.api.endpoints import login
from app.app.crud.login_crud import reset_password
from app.app.db.init_db import init_db

app = FastAPI()

init_db()
app.include_router(login.router)

init_db()
app.include_router(reset_password.router)