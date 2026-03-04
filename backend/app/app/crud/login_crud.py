from fastapi import HTTPException
from app.app.models.ecommerce_user import Users
from app.app.models.ecommerce_token import EcommerceToken
from starlette import status
from sqlalchemy.orm import Session
from app.app.core.security import verify_password, create_token
from sqlalchemy import or_
from abc import ABC,abstractmethod

class LoginAbstract(ABC):
    @abstractmethod
    def user_validation():
        pass
    @abstractmethod
    def token_generation():
        pass

    
class LoginDetails(LoginAbstract):
    def __init__(self,db:Session, user_data):
        self.db = db
        self.user_data = user_data
class LoginDetails(LoginAbstract):
    def __init__(self,db:Session, user_data):
        self.db = db
        self.user_data = user_data
    def user_validation(self):
        user = self.db.query(Users).filter(
            or_(
            Users.username == self.user_data.username,
            Users.email == self.user_data.email,
            Users.status == 1)
            ).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")
        
        if user.is2fa:
           return self.otp_sent(user)
        
        verify_user_password = verify_password(self.user_data.password,user.password)
        
        if verify_user_password:
            user.otp = None
            user_token = self.token_generation(user.user_id)
            return {"msg":"login successfull",
                    "token" : user_token }
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Wrong Password")
        
        
    def token_generation(self,user_id):
        user = self.db.query(Users).filter(EcommerceToken.user_id == user_id).first()
        if not user:
            self.db.query(EcommerceToken).add({
                "user_id" : user_id,
                "token" : create_token({"sub":str(user_id)})
            })
        user.token = create_token({"sub":str(user_id)})
        self.db.commit()
        self.db.refresh(user)
        return user.token
