from fastapi import HTTPException
from app.app.models.ecommerce_user import Users
from app.app.models.ecommerce_token import EcommerceToken
from starlette import status
from sqlalchemy.orm import Session
from app.app.crud.otp_crud import OtpSent
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
    # @abstractmethod
    # def reset_password():
    #     pass


class LoginDetails(LoginAbstract):
    def __init__(self,db:Session, user_data):
        self.db = db
        self.user_data = user_data
    def user_validation(self):

        user = self.db.query(Users).filter(
            or_(
                Users.username == self.user_data.username,
                Users.email == self.user_data.email
            ),
            Users.status == "active"
        ).first()

    

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        if user.is2FA:
            return OtpSent(self.db, user)

        verify_user_password = verify_password(
            self.user_data.password,
            user.password
        )

        if not verify_user_password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Wrong Password"
            )

        token = self.token_generation(user.user_id)

        return {
            "msg": "Login successful",
            "token": token
        }
        
        
    def token_generation(self,user_id):

        user_token = (
            self.db.query(EcommerceToken)
            .filter(EcommerceToken.user_id == user_id)
            .first()
        )

        token = create_token({"sub": str(user_id)})

        if not user_token:
            user_token = EcommerceToken(
                user_id=user_id,
                hashed_token=token
            )
            self.db.add(user_token)

        else:
            user_token.hashed_token = token

        self.db.commit()
        self.db.refresh(user_token)

        return user_token.hashed_token
    
    

