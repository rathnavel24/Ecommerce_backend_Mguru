from app.app.models.ecommerce_userotp import EcommerceUserOtp
from app.app.models.ecommerce_user import Users
from datetime import datetime
from app.app.core.security import create_access_token

class VerifyOTPCRUD:

    def __init__(self, db, otp_key, otp):
        self.db = db
        self.otp_key = otp_key
        self.otp = otp

    def verify(self):

        otp_record = self.db.query(EcommerceUserOtp).filter(
            EcommerceUserOtp.reset_key == self.otp_key,
            EcommerceUserOtp.is_used == False
        ).first()

        if not otp_record:
            raise Exception("Invalid OTP key")

        if otp_record.expires_at < datetime.now():
            raise Exception("OTP expired")

        if str(otp_record.otp) != str(self.otp):
            raise Exception("Incorrect OTP")

        otp_record.is_used = True
        self.db.commit()

        user = self.db.query(Users).filter(
            Users.user_id == otp_record.user_id
        ).first()

        token = create_access_token(
            data={"user_id": otp_record.user_id,
                  "role": user.type}
        )

        return {
            "token": token,
            "token_type": "bearer"
        }