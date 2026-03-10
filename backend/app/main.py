from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.app.api.endpoints import login
from app.app.api.endpoints import verifyotp
from app.app.api.endpoints import forgot_password
from app.app.api.endpoints import reset_password
from app.app.api.endpoints import address
from app.app.api.endpoints import order


app = FastAPI()





app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login.router)
app.include_router(verifyotp.router)
app.include_router(forgot_password.router)
app.include_router(reset_password.router)
app.include_router(address.router)
app.include_router(order.router)

