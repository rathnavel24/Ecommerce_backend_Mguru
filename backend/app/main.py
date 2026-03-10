from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.app.api.endpoints import login
from app.app.api.endpoints import verifyotp
from app.app.api.endpoints import forgot_password
from app.app.api.endpoints import reset_password
from app.app.api.endpoints import category
from app.app.api.endpoints import productinfo
from app.app.api.endpoints import inventory


from app.app.api.endpoints import changepassword
from app.app.api.endpoints import getuserinfo
from app.app.api.endpoints import signup
from app.app.api.endpoints import resendotp
app = FastAPI()





app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(signup.router)
app.include_router(login.router)
app.include_router(verifyotp.router)
app.include_router(forgot_password.router)
app.include_router(reset_password.router)
app.include_router(category.router)
app.include_router(productinfo.router)
app.include_router(inventory.router)
app.include_router(changepassword.router)
app.include_router(getuserinfo.router)
app.include_router(resendotp.router)
