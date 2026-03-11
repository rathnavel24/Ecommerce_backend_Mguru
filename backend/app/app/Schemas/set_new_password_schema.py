from pydantic import BaseModel


class SetNewPassword(BaseModel):
    otp_key: str
    new_password: str