from app.app.db.base import Base
from sqlalchemy import Column,String,TIMESTAMP,Integer,func,ForeignKey,Enum
from sqlalchemy.orm import relationship

class EcommerceCart(Base):
    __tablename__ = 'cart'

    card_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.user_id"))
    product_id = Column(Integer,ForeignKey("product_info.product_id"))
    quantity = Column(Integer)
    status = Column(Enum("active","inactive","deleted"))
    created_at = Column(TIMESTAMP, default=func.now())
    update_at = Column(TIMESTAMP, default=func.now())
    created_by = Column(String(100))

