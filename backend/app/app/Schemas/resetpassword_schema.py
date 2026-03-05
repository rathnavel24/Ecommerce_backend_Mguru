from pydantic import BaseModel

class ResetPassword(BaseModel):
    user_id : str
    email : str
    old_password : str
    new_password : str
    