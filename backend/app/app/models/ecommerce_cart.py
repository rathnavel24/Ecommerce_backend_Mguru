from app.app.db.base import Base
from sqlalchemy import Column,String,TIMESTAMP,Integer,func,ForeignKey,Enum
from sqlalchemy.orm import relationship

class EcommerceCart(Base):
    __tablename__ = 'cart'

    cart_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    product_id = Column(Integer, ForeignKey("product_info.product_id"))

    quantity = Column(Integer)
    status = Column(Enum("active","inactive","deleted"))
    created_at = Column(TIMESTAMP, default=func.now())
    update_at = Column(TIMESTAMP, default=func.now())
    created_by = Column(String(100))

    user = relationship("Users", back_populates="cart")
    product = relationship("EcommerceProductInfo", back_populates="cart_items")

