# from app.app.db.base import Base
# from sqlalchemy import Column, String, TEXT, SmallInteger, TIMESTAMP, Integer, Boolean, func, ForeignKey
# from sqlalchemy.orm import relationship

# class EcommerceUserRole(Base):
#     __tablename__ = 'user_role'
    
#     userrole_id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("User.user_id"))
#     role_id = Column(Integer, ForeignKey("roles.role_id"))
 
#     user = relationship("Users", back_populates="ecomuser")
#     userrole = relationship("EcommerceRoles", back_populates="user_role")