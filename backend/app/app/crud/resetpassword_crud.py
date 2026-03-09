# resetting password
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.app.Schemas.resetpassword_schema import ResetPassword
from app.app.core.security import get_password_hash
from app.app.models.ecommerce_user import Users
from app.app.models.ecommerce_userotp import EcommerceUserOtp
from datetime import datetime

def reset_password(db: Session, data: ResetPassword):

    record = db.query(EcommerceUserOtp).filter(
        EcommerceUserOtp.reset_key == data.token,
        EcommerceUserOtp.is_used == False
    ).first()

    if not record:
        raise HTTPException(status_code=401, detail="Invalid token")

    if record.expires_at < datetime.now():
        raise HTTPException(status_code=400, detail="OTP expired")

    user = db.query(Users).filter(
        Users.user_id == record.user_id
    ).first()

    user.password = get_password_hash(data.new_password)

    record.is_used = True

    db.commit()

    return {"message": "Password reset successful"}