from pydantic import BaseModel


class VerifyForgotOTP(BaseModel):
    otp_key: str
    otp: str