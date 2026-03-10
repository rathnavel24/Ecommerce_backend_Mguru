from app.app.models.ecommerce_user import Users
from app.app.models.ecommerce_userotp import EcommerceUserOtp
from app.app.core.security import generate_otp, generate_otp_key
from datetime import datetime, timedelta
from app.app.crud.otp_crud import otp_sent

class ForgotPasswordCRUD:

    def __init__(self, db, email):
        self.db = db
        self.email = email

    def send_otp(self):

        user = self.db.query(Users).filter(
            Users.email == self.email
        ).first()

        if not user:
            raise Exception("User not found")

        otp = generate_otp()
        reset_key = generate_otp_key()

        otp_entry = EcommerceUserOtp(
            user_id=user.user_id,
            otp=otp,
            reset_key=reset_key,
            expires_at=datetime.now() + timedelta(minutes=5),
            is_used=False
        )

        self.db.add(otp_entry)
        self.db.commit()

        otp_sent(user.email, otp)

        return {
            "message": "OTP sent successfully",
            "otp_key": reset_key
        }