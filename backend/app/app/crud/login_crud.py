from fastapi import HTTPException
from starlette import status
from sqlalchemy.orm import Session
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