from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

from enum import Enum

class ProductCreate(BaseModel):
    product_name: str
    category_id: int
    product_price: Decimal
    discount_per: Optional[Decimal] = None
    product_description: Optional[str] = None
    image_url: Optional[str] = None
    status: Optional[str] = "active"


class UpdateProduct(BaseModel):
    product_name: Optional[str] = None
    category_id: Optional[int] = None
    product_price: Optional[Decimal] = None
    discount_per: Optional[Decimal] = None
    product_description: Optional[str] = None
    image_url: Optional[str] = None
    status: Optional[Enum] = None
    