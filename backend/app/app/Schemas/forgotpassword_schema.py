from pydantic import BaseModel

class ForgotPassword(BaseModel):
    email : str
    # otp : int
    # new_password : str
    