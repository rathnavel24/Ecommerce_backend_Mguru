from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.app.api.endpoints import login
from app.app.api.endpoints import verifyotp
from app.app.api.endpoints import forgot_password
from app.app.api.endpoints import address
from app.app.api.endpoints import order
from app.app.api.endpoints import category
from app.app.api.endpoints import productinfo
from app.app.api.endpoints import inventory
from app.app.api.endpoints import changepassword
from app.app.api.endpoints import getuserinfo
from app.app.api.endpoints import signup
from app.app.api.endpoints import resendotp
from app.app.api.endpoints import forgot_password
from app.app.api.endpoints import verify_forgot_otp
from app.app.api.endpoints import set_new_password
from app.app.api.endpoints import payments
from app.app.api.endpoints import cart
from app.app.api.endpoints import checkout
from app.app.api.endpoints import orderitems

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
app.include_router(verify_forgot_otp.router)
app.include_router(set_new_password.router)
app.include_router(address.router)
app.include_router(order.router)
app.include_router(category.router)
app.include_router(productinfo.router)
app.include_router(inventory.router)
app.include_router(changepassword.router)
app.include_router(getuserinfo.router)
app.include_router(resendotp.router)
app.include_router(payments.router)
app.include_router(cart.router)
app.include_router(checkout.router)
app.include_router(orderitems.router)
