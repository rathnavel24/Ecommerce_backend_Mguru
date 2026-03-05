from typing import Optional

from pydantic import BaseModel,EmailStr,Field

class UserSignUp(BaseModel):
    username : str
    email : EmailStr
    password : str 
    type : Optional[str] = 'user'
    