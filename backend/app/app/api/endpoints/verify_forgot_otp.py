from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.app.db.session import sessionLocal
from app.app.Schemas.verify_forgot_otp_schema import VerifyForgotOTP
from app.app.crud.verify_forgot_otp_crud import VerifyForgotOTPCRUD
from app.app.api.deps import get_db

router = APIRouter(tags=["login"])



@router.post("/verify_forgot_otp")
async def verify_forgot_otp(data: VerifyForgotOTP, db: Session = Depends(get_db)):
    try:
        return VerifyForgotOTPCRUD(db, data.otp_key, data.otp).verify()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))