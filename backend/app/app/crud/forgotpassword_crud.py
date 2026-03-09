from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import or_
from sqlalchemy.orm import Session
from datetime import datetime,timedelta
from app.app.Schemas import forgotpassword_schema
from app.app.Schemas.forgotpassword_schema import ForgotPassword
from pydantic import BaseModel
from jose import jwt, JWTError
from passlib.context import CryptContext
from app.app.core.security import verify_password, get_password_hash
from app.app.api.deps import get_db
from app.app.crud.otp_crud import OtpSent
from app.app.models.ecommerce_userotp import EcommerceUserOtp
from app.app.models.ecommerce_user import Users
from app.app import models
import random

def forgot_password(db: Session, email: str):
    user = db.query(Users).filter(
        Users.email == email
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Email not found"
        )
    
    OTP = OtpSent(db,user)

    return OTP
