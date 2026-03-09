from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.app.api.endpoints import login
from app.app.api.endpoints import verifyotp





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