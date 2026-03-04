from app.app.db.base import Base
from sqlalchemy import Column,String,TIMESTAMP,Integer,func,ForeignKey,Enum
from sqlalchemy.orm import relationship

class EcommerceCategories(Base):
    __tablename__ = 'categories'

    categories_id = Column(Integer,ForeignKey("product_info.categorie_id"))
    name = Column(String(255))
    parent_id = Column(Integer,ForeignKey("categories.categories_id"))
    status = Column(Enum("active","inactive","deleted"))
    created_at = Column(TIMESTAMP,default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now())
    created_by = Column(String(100))