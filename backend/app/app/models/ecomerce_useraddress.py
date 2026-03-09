# from app.app.db.base import Base
# from sqlalchemy import Column,String,TEXT,Integer,Boolean,ForeignKey
# from sqlalchemy.orm import relationship

# class EcommerceUserAddress(Base):
#     __tablename__ = 'user_address'

#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("users.user_id"))

#     address_line1 = Column(TEXT)
#     address_line2 = Column(TEXT)
#     city = Column(String(50))
#     state = Column(String(50))
#     country = Column(String(50))
#     pincode = Column(String(10))
#     isdefault = Column(Boolean)

#     user = relationship("Users", back_populates="addresses")
#     orders = relationship("EcommerceOrder", back_populates="address")