from app.app.db.base import Base
from sqlalchemy import Column,String,TIMESTAMP,Integer,func,ForeignKey,Enum
from sqlalchemy.orm import relationship

class EcommerceInventory(Base):
    __tablename__ = 'inventory'

    inventory_id = Column(Integer, primary_key=True)
    product_id = Column(Integer,ForeignKey("product_info.product_id"))
    stock_quantity = Column(Integer)
    reserved_quantity = Column(Integer)
    last_restocked_at = Column(TIMESTAMP,default=func.now())
    status = Column(Enum("active","inactive","deleted"))
    created_at = Column(TIMESTAMP,default=func.now())
    updated_at = Column(TIMESTAMP,default=func.mow())
    created_by = Column(String(100))

    product_inv = relationship("EcommerceProductInfo", back_populates="itemsinventory")