from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.app.Schemas.userlogin_schema import LoginRequest, VerifyOtp, ResendOtp
from app.app.crud.otplogin_crud import  verify_otp, resend_otp
from app.app.api.deps import get_db

router = APIRouter()


@router.post("/verify-otp")
def verify(data: VerifyOtp, db: Session = Depends(get_db)):
    return verify_otp(db, data.email, data.otp)


@router.post("/resend-otp")
def resend(data: ResendOtp, db: Session = Depends(get_db)):
    return resend_otp(db, data)