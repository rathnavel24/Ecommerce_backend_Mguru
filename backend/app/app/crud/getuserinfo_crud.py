from fastapi import HTTPException
from starlette import status 
from app.app.models.ecommerce_user import Users
from starlette import status
from sqlalchemy.orm import Session
from abc import ABC,abstractmethod

class GetUserInfoAbstract(ABC):

    @abstractmethod
    def getuserinfo():
        pass

class GetUserInfo(GetUserInfoAbstract):
    def __init__(self,db:Session,user_id):
        self.user_id = user_id
        self.db = db

    def getuserinfo(self):

        try:
            result =self.db.query(Users.email,Users.username).filter(
                Users.user_id == self.user_id).first()
            
            if not result :
                return False
            
            return {
            "email": result.email,
            "username": result.username
            }


        except Exception as e:
            raise e