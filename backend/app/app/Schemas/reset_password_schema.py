from pydantic import BaseModel

class ResetPassword(BaseModel):
    otp_key: str
    otp: str
    new_password: str