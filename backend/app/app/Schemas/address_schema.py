from pydantic import BaseModel
from typing import Optional

class CreateAddress(BaseModel):
    address_line1: str
    address_line2: str
    city: str
    state: str
    country: str
    pincode: str
    isdefault: bool


class UpdateAddress(BaseModel):
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    pincode: Optional[str] = None
    isdefault: Optional[bool] = None