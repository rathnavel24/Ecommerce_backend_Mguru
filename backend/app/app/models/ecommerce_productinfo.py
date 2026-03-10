from app.app.db.base import Base
from sqlalchemy import Column,String,TEXT,TIMESTAMP,Integer,func,DECIMAL,Enum,ForeignKey
from sqlalchemy.orm import relationship
import random 
import string

def generate_sku():
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(10))


class EcommerceProductInfo(Base):
    __tablename__ = 'product_info'

    product_id = Column(Integer, primary_key=True)

    product_name = Column(String(255))
    categorie_id = Column(Integer, ForeignKey("categories.categories_id"))

    price = Column(DECIMAL(10,2))
    discount_percent = Column(DECIMAL(10,2))

    description = Column(TEXT)
    image_url = Column(TEXT)
    sku = Column(String(100), unique=True, default=generate_sku)

    status = Column(Enum('active','inactive','deleted'))

    createdat = Column(TIMESTAMP, default=func.now())
    updatedat = Column(TIMESTAMP, default=None, onupdate=func.now())
    createdby = Column(String(50), default='ADMIN')

    category = relationship("EcommerceCategories", back_populates="products")
    order_items = relationship("EcommerceOrderItems", back_populates="product")
    inventory = relationship("EcommerceInventory", back_populates="product")
    cart_items = relationship("EcommerceCart", back_populates="product")
