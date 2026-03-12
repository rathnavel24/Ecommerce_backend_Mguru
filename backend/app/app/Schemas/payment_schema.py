from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class PaymentCreate(BaseModel):

    order_id : int
    user_id : int
    payment_gateway : str
    amount : Decimal
    payment_method : str
    payment_status : Optional[str] = "pending"

class PaymentUpdate(BaseModel):
    
    payment_gateway: Optional[str] = None
    amount: Optional[Decimal] = None
    payment_method: Optional[str] = None
    payment_status: Optional[str] = None





    




     