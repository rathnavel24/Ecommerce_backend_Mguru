from app.app.db.base import Base
from sqlalchemy import Column,String,TEXT,SmallInteger,TIMESTAMP,Integer,Boolean,func,ForeignKey,DECIMAL,Enum
from sqlalchemy.orm import relationship

class EcommerceOrder(Base):
    __tablename__ = 'order'

    order_id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey("User.user_id"))
    total_price = Column(DECIMAL(10,2))
    shipping_address = Column(Integer, ForeignKey("user_address.id"))
    order_status = Column(Enum("placed","shipped","delivered","cancelled"))
    status = Column(Enum("active","inactive","deleted"))
    created_at = Column(TIMESTAMP,default=func.now())
    updated_at = Column(TIMESTAMP,default=func.now())
    created_by = Column(String(100))

    userorder = relationship("EcommercePayments", back_populates="userpay")
    useritmes = relationship("EcommerceOrderItmes", back_populates="userorder")
    useraddress = relationship("EcommerceUserAddress", back_populates="address_user")
