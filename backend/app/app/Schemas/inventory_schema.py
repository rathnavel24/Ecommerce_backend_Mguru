from pydantic import BaseModel
from typing import Optional

class InventoryCreate(BaseModel):

    product_id: int
    stock_quantity :int
    reserved_quantity :int
    status : str
    created_by :str

class InventoryUpdate(BaseModel):

    stock_quantity : int
    reserved_quantity : int
    status : str
