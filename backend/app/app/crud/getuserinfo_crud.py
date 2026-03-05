from fastapi import HTTPException
from starlette import status 
from app.app.models.ecommerce_user import Users
from starlette import status
from sqlalchemy.orm import Session
from app.app.core.security import decode_token
from abc import ABC,abstractmethod

class GetUserInfoAbstract(ABC):

    @abstractmethod
    def getuserinfo():
        pass

class GetUserInfo(GetUserInfoAbstract):
    def __init__(self,db:Session,token):
        self.token = token
        self.db = db

    def getuserinfo(self):

        try:
            user = decode_token(self.token)
            result =self.db.query(Users.email,Users.username).filter(
                Users.user_id == user.get("sub")).first()
            
            if not result :
                return False
            return {
            "email": result.email,
            "username": result.username
            }


        except Exception as e:
            raise e

