from pydantic import BaseModel

class CreateOrder(BaseModel):
    user_id : int
    total_price : float
    shipping_address : int


class UpdateOrderStatus(BaseModel):
    order_status : str     