from app.app.db.base import Base
from datetime import datetime, timedelta
from sqlalchemy import Column, String, TIMESTAMP, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class EcommerceToken(Base):
    __tablename__ = "token"

    token_id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.user_id"))

    hashed_token = Column(String(255))

    expires_at = Column(
        TIMESTAMP,
        default=lambda: datetime.utcnow() + timedelta(minutes=5)
    )

    created_at = Column(TIMESTAMP, default=func.now())

    user = relationship("Users", back_populates="token")