from sqlalchemy import Column, Integer, String, Float, Boolean, TIMESTAMP, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.app.db.base import Base

class Users(Base):
    __tablename__ = "User"

    user_id = Column(Integer, primary_key=True)
    username = Column(String(100))
    email = Column(String(255), unique=True)
    password = Column(String(255))
    type = Column(String(100))
    is2FA = Column(Boolean, default=0)
    status = Column(Enum("active", "inactive", "deleted"))
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now())
    created_by = Column(String(100))

    # user_role = relationship("EcommerceUserRole", back_populates="userrole")
    user_otp = relationship("EcommerceUserOtp", back_populates="userotp")
    token = relationship("EcommerceToken", back_populates="ecom_token")
    user_address = relationship("EcommerceUserAddress", back_populates="useraddress")
    cart = relationship("EcommerceCart", back_populates="ecom_cart")
    userorder= relationship("EcommerceOrder", back_populates="userpay") 
    userpay= relationship("EcommercePayments", back_populates="userorder") 

