from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Enum
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
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())
    created_by = Column(String(100))
    

