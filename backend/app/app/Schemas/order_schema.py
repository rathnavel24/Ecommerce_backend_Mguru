from pydantic import BaseModel
from typing import Optional
from decimal import Decimal


class OrderCreate(BaseModel):
    shipping_address: int
    total_price: Decimal


class OrderStatusUpdate(BaseModel):
    order_status : str


class OrderResponse(BaseModel):
    order_id : int
    user_id : int
    total_price : float
    shipping_address : int
    order_status : str
    status : str

    class Config:
        from_attributes = True

class OrderBuyNow(BaseModel):
    product_id : str
    quantity : int
    address_id : int



    

