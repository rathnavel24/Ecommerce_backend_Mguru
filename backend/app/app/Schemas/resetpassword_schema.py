from pydantic import BaseModel

class ResetPassword(BaseModel):
    user_id : int
    email : str
    existing_password : str
    new_password : str


