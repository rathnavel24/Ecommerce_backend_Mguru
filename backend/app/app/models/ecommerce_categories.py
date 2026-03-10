from app.app.db.base import Base
from sqlalchemy import Column,String,TIMESTAMP,Integer,func,ForeignKey,Enum,TEXT
from sqlalchemy.orm import relationship

class EcommerceCategories(Base):
    __tablename__ = 'categories'

    categories_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    parent_id = Column(Integer, ForeignKey("categories.categories_id"))
    image_url = Column(TEXT)
    status = Column(Enum("active","inactive","deleted"))
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now())
    created_by = Column(String(100))

    products = relationship("EcommerceProductInfo", back_populates="category")

    parent = relationship("EcommerceCategories",remote_side=[categories_id],backref="children")