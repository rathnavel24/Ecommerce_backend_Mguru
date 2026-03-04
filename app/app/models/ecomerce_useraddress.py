from app.app.db.base import Base
from sqlalchemy import Column,String,TEXT,SmallInteger,TIMESTAMP,Integer,Boolean,func
from sqlalchemy.orm import relationship

class EcommerceUserAddress(Base):
    __tablename__ = 'user_address'