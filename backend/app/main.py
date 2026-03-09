from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.app.api.endpoints import login
from app.app.api.endpoints import signup
from app.app.api.endpoints import getuserinfo
from app.app.api.endpoints import category
from app.app.api.endpoints import resetpassword
from app.app.db.init_db import init_db
from app.app.api.endpoints import otplogin
# from app.app.api.endpoints import order
from app.app.api.endpoints import address


# from app.app.api.order_router import router as order_router


app = FastAPI()

init_db()




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
# app.include_router(forgotpassword.router)
app.include_router(resetpassword.router)
app.include_router(otplogin.router)
app.include_router(category.router)
app.include_router(address.router)
