from pydantic import BaseModel


class OrderItemDetailedResponse(BaseModel):

    orderitems_id: int
    order_id: int

    product_id: int
    product_name: str
    image_url: str
    category: str

    price: float
    quantity: int
    total_price: float

    class Config:
        orm_mode = True