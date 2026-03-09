from pydantic import BaseModel

class CreateAddress(BaseModel):
    user_id: int
    address_line1: str
    address_line2: str
    city: str
    state: str
    country: str
    pincode: str
    isdefault: bool


class UpdateAddress(BaseModel):
    address_line1: str
    address_line2: str
    city: str
    state: str
    country: str
    pincode: str
    isdefault: bool