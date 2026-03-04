from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.app.db.base import Base

class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    username = Column(String(100))
    email = Column(String(255), unique=True)
    password = Column(String(255))
    type = Column(String(100))
    is2FA = Column(Boolean, default=False)
    status = Column(Enum("active", "inactive", "deleted"))
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now())
    created_by = Column(String(100))

    user_otp = relationship("EcommerceUserOtp", back_populates="user")
    token = relationship("EcommerceToken", back_populates="user")
    addresses = relationship("EcommerceUserAddress", back_populates="user")
    cart = relationship("EcommerceCart", back_populates="user")
    orders = relationship("EcommerceOrder", back_populates="user")
    payments = relationship("EcommercePayments", back_populates="user")