from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class ProductCreate(BaseModel):
    product_name: str
    category_id: int
    product_price: Decimal
    discount_per: Optional[Decimal] = None
    product_description: Optional[str] = None
    image_url: Optional[str] = None
    status: Optional[str] = "active"