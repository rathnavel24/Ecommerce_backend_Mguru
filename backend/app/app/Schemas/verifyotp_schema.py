from pydantic import BaseModel


class VerifyOtp(BaseModel):
    otp_key: str
    otp: str