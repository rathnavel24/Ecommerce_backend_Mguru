from app.app.db.base import Base
from sqlalchemy import Column,String,TEXT,SmallInteger,TIMESTAMP,Integer,Boolean,func,ForeignKey,DECIMAL,Enum
from sqlalchemy.orm import relationship

class EcommerceOrder(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))

    total_price = Column(DECIMAL(10,2))
    shipping_address = Column(Integer, ForeignKey("user_address.id"))

    order_status = Column(Enum("placed","shipped","delivered","cancelled"))
    status = Column(Enum("active","inactive","deleted"))

    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())
    created_by = Column(String(100))

    user = relationship("Users", back_populates="orders")
    items = relationship("EcommerceOrderItems", back_populates="order")
    address = relationship("EcommerceUserAddress", back_populates="orders")
    payment = relationship("EcommercePayments", back_populates="order")
