from datetime import datetime, timedelta
import secrets
from sqlalchemy.orm import Session
from app.app.models.ecommerce_userotp import EcommerceUserOtp
from app.app.core.security import generate_otp

OTP_EXPIRE_MINUTES = 10


def create_otp(db: Session, user_id: int, otp_type: str):

    otp = generate_otp()
    reset_key = secrets.token_urlsafe(32)

    record = EcommerceUserOtp(
        user_id=user_id,
        otp=otp,
        otp_type=otp_type,
        reset_key=reset_key,
        expires_at=datetime.utcnow() + timedelta(minutes=OTP_EXPIRE_MINUTES),
        is_used=False
    )

    db.add(record)
    db.commit()

    return otp, reset_key


def verify_otp(db: Session, user_id: int, otp: str):

    record = db.query(EcommerceUserOtp).filter(
        EcommerceUserOtp.user_id == user_id,
        EcommerceUserOtp.otp == otp,
        EcommerceUserOtp.is_used == False
    ).first()

    if not record:
        return None

    if record.expires_at < datetime.utcnow():
        return None

    record.is_used = True
    db.commit()

    return record