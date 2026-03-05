from pydantic import BaseModel,EmailStr
from typing import Optional

class UserLogin(BaseModel):
    username : Optional[str] = None
    email : Optional[EmailStr] = None
    password : str

class LoginRequest(BaseModel):
    email : EmailStr
    password : str

class VerifyOtp(BaseModel):
    email : EmailStr
    otp : str

class ResendOtp(BaseModel):
    email :EmailStr