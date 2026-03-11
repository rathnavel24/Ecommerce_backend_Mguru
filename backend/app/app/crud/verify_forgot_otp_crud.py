from app.app.models.ecommerce_userotp import EcommerceUserOtp
from datetime import datetime


class VerifyForgotOTPCRUD:

    def __init__(self, db, reset_key, otp):
        self.db = db
        self.reset_key = reset_key
        self.otp = otp

    def verify(self):

        otp_record = self.db.query(EcommerceUserOtp).filter(
            EcommerceUserOtp.reset_key == self.reset_key,
            EcommerceUserOtp.is_used == False
        ).first()

        if not otp_record:
            raise Exception("Invalid reset key")

        if otp_record.expires_at < datetime.utcnow():
            raise Exception("OTP expired")

        if str(otp_record.otp) != str(self.otp):
            raise Exception("Incorrect OTP")

        otp_record.otp_verified = True

        self.db.commit()

        return {
            "message": "OTP verified successfully"
        }