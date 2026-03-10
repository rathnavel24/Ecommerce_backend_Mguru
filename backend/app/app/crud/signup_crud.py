from app.app.models.ecommerce_user import Users
from app.app.core.security import get_password_hash
from sqlalchemy import or_
from sqlalchemy.orm import Session
from abc import ABC,abstractmethod
from fastapi import HTTPException
from starlette import status
class SignUpAbstract(ABC):

    @abstractmethod
    def user_signup():
        pass
    
    @abstractmethod
    def user_verification():
        pass

    

class SignUpDetails(SignUpAbstract):
    def __init__(self, db:Session, new_user):
        self.db = db
        self.new_user = new_user
    
    def user_signup(self):

        if self.user_verification():
            self.db.add(Users(
                username = self.new_user.username,
                email =  self.new_user.email,
                password = get_password_hash(self.new_user.password),
                type = self.new_user.type
                ))
            self.db.commit()
            return {
                "msg" : "User Created Successfully"
            }
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="User already Exists")

    def user_verification(self) -> bool: 
        user = self.db.query(Users).filter(
            or_(
                Users.username == self.new_user.username,
                Users.email == self.new_user.email
                

            ),
            Users.status == "active"
        ).first()

        if not user:
            return True
        else:
            return False