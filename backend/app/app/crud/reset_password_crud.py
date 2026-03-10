from app.app.models.ecommerce_userotp import EcommerceUserOtp
from app.app.models.ecommerce_user import Users
from app.app.core.security import hash_password
from datetime import datetime


class ResetPasswordCRUD:

    def __init__(self, db, reset_key, otp, new_password):
        self.db = db
        self.reset_key = reset_key
        self.otp = otp
        self.new_password = new_password

    def reset(self):

        otp_record = self.db.query(EcommerceUserOtp).filter(
            EcommerceUserOtp.reset_key == self.reset_key,
            EcommerceUserOtp.is_used == False
        ).first()

        if not otp_record:
            raise Exception("Invalid reset key")

        if otp_record.expires_at < datetime.now():
            raise Exception("OTP expired")

        if str(otp_record.otp) != str(self.otp):
            raise Exception("Incorrect OTP")

        user = self.db.query(Users).filter(
            Users.user_id == otp_record.user_id
        ).first()

        user.password = hash_password(self.new_password)

        otp_record.is_used = True

        self.db.commit()

        return {
            "message": "Password reset successfully"
        }