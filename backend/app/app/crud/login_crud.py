from fastapi import HTTPException
from starlette import status
from datetime import datetime,timedelta
from app.app.models.ecommerce_userotp import EcommerceUserOtp
from app.app.models.ecommerce_user import Users
from app.app.core.security import verify_password, create_access_token
from app.app.crud.otp_crud import otp_sent
from app.app.core.security import generate_otp , generate_otp_key
class LoginUser:

    def __init__(self, db, email, password):
        self.db = db
        self.email = email
        self.password = password

    def login(self):

        user = self.db.query(Users).filter(
            Users.email == self.email
        ).first()

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="no user found")

        if not verify_password(self.password, user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Wrong password")

        if user.is2FA:

            otp = generate_otp()
            otp_key = generate_otp_key()

            otp_entry = EcommerceUserOtp(
                user_id=user.user_id,
                otp=otp,
                reset_key=otp_key,
                expires_at=datetime.now() + timedelta(minutes=5),
                is_used=False
            )

            self.db.add(otp_entry)
            self.db.commit()


            otp_sent(user.email, otp)
            print(otp)
            return {
                "timer": 600,
                "otp_key": otp_key
            }

        token = create_access_token(
            data={"user_id": user.user_id,
                  "role": user.type
                })

        return {
            "token": token,
            "token_type": "bearer",
            "user_type" : user.type
        }