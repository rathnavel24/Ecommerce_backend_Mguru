from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime,timedelta
from app.app.models.ecommerce_userotp import EcommerceUserOtp
from app.app.models.ecommerce_user import Users
import secrets
from datetime import datetime, timedelta
from app.app.models.ecommerce_userotp import EcommerceUserOtp
from app.app.core.security import generate_otp

def forgot_password(db: Session, email: str):

    user = db.query(Users).filter(Users.email == email).first()

    if not user:
        raise HTTPException(status_code=404, detail="Email not found")

    otp = generate_otp()

    reset_key = secrets.token_urlsafe(32)

    record = EcommerceUserOtp(
        user_id=user.user_id,
        otp=otp,
        reset_key=reset_key,
        expires_at=datetime.now() + timedelta(minutes=10),
        is_used=False
    )

    db.add(record)
    db.commit()
    
    print("OTP:", otp)

    return {
        "message": "OTP sent",
        "reset_key": reset_key
    }
