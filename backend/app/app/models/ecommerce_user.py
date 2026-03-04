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
    is2FA = Column(Boolean, default=0)
    status = Column(Enum("active", "inactive", "deleted"))
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now())
    created_by = Column(String(100))

    user_role = relationship("ecommerce_user_role", back_populates="userrole")
    user_otp = relationship("ecommerce_userotp", back_populates="userotp")
    token = relationship("ecommerce_token", back_populates="ecom_token")
    user_address = relationship("ecommerce_useraddress", back_populates="user_address")
    cart = relationship("ecommerce_cart", back_populates="ecom_cart")
    order= relationship("ecommerce_order", back_populates="ecom_order") 
    payments= relationship("ecommerce_payments", back_populates="ecom_payments") 

