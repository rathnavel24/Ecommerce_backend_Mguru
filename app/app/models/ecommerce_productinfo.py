from app.app.db.base import Base
from sqlalchemy import Column,String,TEXT,TIMESTAMP,Integer,func,DECIMAL,Enum
from sqlalchemy.orm import relationship

class EcommerceProductInfo(Base):
    __tablename__ = 'product_info'
    product_id = Column(Integer,primary_key=True)
    product_name = Column(String(255))
    categorie_id = Column(Integer)
    price  = Column(DECIMAL(10,2))
    discount_percent = Column(DECIMAL(10,2))
    description = Column(TEXT)
    image_url = Column(TEXT)
    sku = Column(String(100))
    status = Column(Enum('active','inactive','deleted'))
    createdat = Column(TIMESTAMP,default= func.now())
    updatedat = Column(TIMESTAMP,default=None,onupdate=func.now())
    createdby = Column(String(50),default='ADMIN')