from datetime import datetime
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.app.models.ecommerce_user import Users
from app.app.models.ecommerce_userotp import EcommerceUserOtp
from app.app.models.ecommerce_user import Users
from app.app.core.security import create_token


def verify_otp(db: Session, email: str, otp: str):

    user = db.query(Users).filter(Users.email == email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    record = db.query(EcommerceUserOtp).filter(
        EcommerceUserOtp.user_id == user.user_id,
        EcommerceUserOtp.otp == otp
    ).first()

    if not record:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    if record.expires_at < datetime.now():
        db.delete(record)
        db.commit()
        raise HTTPException(status_code=400, detail="OTP expired")

    access_token = create_token(
        data={"sub": str(user.user_id)}
    )

    db.delete(record)
    db.commit()

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }