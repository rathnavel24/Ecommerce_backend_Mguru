from app.app.db.base import Base
from datetime import timedelta
from sqlalchemy import Column, String, TEXT, SmallInteger, TIMESTAMP, Integer, Boolean, func, ForeignKey
from sqlalchemy.orm import relationship

class EcommerceToken(Base):
    __tablename__ = 'token'

    token_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.user_id"))
    hashed_token = Column(String(255))
    expiresat = Column(TIMESTAMP, default=func.now()+timedelta(minutes=5))
    created_at = Column(TIMESTAMP, default=func.now())

    user = relationship("ecommerce_user", back_populates="token")
