from app.app.db.base import Base
from sqlalchemy import Column,Integer
from sqlalchemy.orm import relationship

class EcommerceRolePermission(Base):
    __tablename__ = 'role_permission'
    role_id = Column(Integer,primary_key=True)
    permission_id = Column(Integer)
