from app.app.db.base import Base
from sqlalchemy import Column, Integer, Boolean, TIMESTAMP, ForeignKey,String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import timedelta
class EcommerceUserOtp(Base):
    __tablename__ = "user_otp"

    otp_id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.user_id"))

    otp = Column(Integer)

    reset_key = Column(String(255))

    expires_at = Column(TIMESTAMP)

    is_used = Column(Boolean, default=False)

    user = relationship("Users", back_populates="user_otp")
