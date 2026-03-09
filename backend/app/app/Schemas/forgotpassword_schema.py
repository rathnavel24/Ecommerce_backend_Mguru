from pydantic import BaseModel

class ForgotPassword(BaseModel):
    token : str
    otp : str
    