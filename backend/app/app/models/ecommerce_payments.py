from app.app.db.base import Base
from sqlalchemy import Column,String,TIMESTAMP,Integer,func,DECIMAL,Enum, ForeignKey
from sqlalchemy.orm import relationship

class EcommercePayments(Base):
    __tablename__ = 'payments'

    payment_id = Column(Integer, primary_key=True)

    order_id = Column(Integer, ForeignKey("orders.order_id"))
    user_id  = Column(Integer, ForeignKey("users.user_id"))

    transaction_id = Column(String(100))
    payment_gateway = Column(String(100))
    amount = Column(DECIMAL(10,2))

    payment_method = Column(String(50))
    payment_status = Column(Enum('pending','success','failed','refunded'))

    paid_at = Column(TIMESTAMP, default=func.now())
    created_at = Column(TIMESTAMP, default=func.now())

    order = relationship("EcommerceOrder", back_populates="payment")
    user = relationship("Users", back_populates="payments")
    
