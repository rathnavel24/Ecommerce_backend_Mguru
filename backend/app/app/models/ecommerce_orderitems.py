from app.app.db.base import Base
from sqlalchemy import Column,String,TIMESTAMP,Integer,func,DECIMAL,Enum,ForeignKey
from sqlalchemy.orm import relationship

class EcommerceOrderItems(Base):
    __tablename__ = 'order_items'

    orderitems_id = Column(Integer, primary_key=True)

    order_id = Column(Integer, ForeignKey("orders.order_id"))
    product_id = Column(Integer, ForeignKey("product_info.product_id"))

    product_name = Column(String(100))
    price = Column(DECIMAL(10,2))
    quantity = Column(Integer)

    status = Column(Enum('active','inactive','deleted'))
    createdat = Column(TIMESTAMP, default=func.now())
    updatedat = Column(TIMESTAMP, default=None, onupdate=func.now())
    createdby = Column(String(50), default='ADMIN')

    order = relationship("EcommerceOrder", back_populates="items")
    product = relationship("EcommerceProductInfo", back_populates="order_items")



