from datetime import datetime, timedelta
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.app.crud.otp_crud import otp_resent , reset_otpkey
from app.app.models.ecommerce_user import Users
from app.app.models.ecommerce_userotp import EcommerceUserOtp
from app.app.models.ecommerce_user import Users
from app.app.core.security import  generate_otp


def verify_otp(db: Session, email: str, otp: str):

    user_id = db.query(Users).filter(Users.email == email).first()

    if not user_id :
        return "no user found"

    record = db.query(EcommerceUserOtp).filter(
        EcommerceUserOtp.user_id == user_id.user_id,
        EcommerceUserOtp.otp == otp
    ).first()

    if not record:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    if record.expires_at < datetime.now():
        db.delete(record)
        db.commit()
        raise HTTPException(status_code=400, detail="OTP expired")

    db.delete(record)
    db.commit()

    return {"message": "Login successful"}


def resend_otp(db: Session, data):

    otp = generate_otp()
    user_id = db.query(Users).filter(Users.email == data.email).first()

    if not user_id :
        return "no user found"

    reset_key = reset_otpkey(user_id.user_id)
    db.query(EcommerceUserOtp).filter(EcommerceUserOtp.user_id == user_id.user_id).update({
        "otp" : otp,
        "reset_key" : reset_key
    })
    db.commit()

    otp_resent(data.email, otp)

    return {"message": "OTP resent",
            "reset_key" : reset_key }