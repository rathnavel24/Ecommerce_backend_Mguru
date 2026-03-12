from pydantic import BaseModel
from typing import Optional

class InventoryCreate(BaseModel):

    product_id: int
    stock_quantity :int
    reserved_quantity :Optional[int] =0
    status : Optional[str] = "active"
    created_by :Optional[str] = "ADMIN"

class InventoryUpdate(BaseModel):

    stock_quantity : int
    reserved_quantity : int
    status : str
