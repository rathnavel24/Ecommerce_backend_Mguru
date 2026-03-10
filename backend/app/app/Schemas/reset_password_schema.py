from pydantic import BaseModel

class ResetPassword(BaseModel):
    reset_key: str
    otp: str
    new_password: str