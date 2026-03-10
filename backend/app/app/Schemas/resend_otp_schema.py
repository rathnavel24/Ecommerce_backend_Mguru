from pydantic import BaseModel

class ResendOTP(BaseModel):
    reset_key: str