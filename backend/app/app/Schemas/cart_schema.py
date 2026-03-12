from pydantic import BaseModel
from typing import List


class CartItem(BaseModel):
    product_id: int
    quantity: int


class CartUpdate(BaseModel):
    items: List[CartItem]


class CartRemove(BaseModel):
    product_ids: List[int]