from pydantic import BaseModel,EmailStr
class userlogin(BaseModel):

    email : EmailStr
    passw : str