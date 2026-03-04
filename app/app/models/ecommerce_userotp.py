from app.app.db.base import Base
from sqlalchemy import Column, String, TEXT, SmallInteger, TIMESTAMP, Integer, Boolean, func, ForeignKey
from sqlalchemy.orm import relationship

class EcommerceUserOtp(Base):
    __tablename__ = 'user_otp'

    otp_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.user_id"))
    otp = Column(Integer)
    expires_at = Column(TIMESTAMP, default=func.now())
    is_used = Column(Boolean)

    user = relationship("ecommerce_user", back_populates="ecomuser1")