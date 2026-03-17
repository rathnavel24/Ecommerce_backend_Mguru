from pydantic import BaseModel
from typing import Optional

class CategoryCreate(BaseModel):
    name:str
    parent_id: Optional[int]= None
    status: Optional[str] = "active"
    image_url : Optional[str]

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    parent_id : Optional[int] = None
    status: Optional[str] = None
    
    