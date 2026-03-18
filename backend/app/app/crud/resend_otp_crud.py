from datetime import datetime, timedelta
from app.app.models.ecommerce_userotp import EcommerceUserOtp
from app.app.models.ecommerce_user import Users
from app.app.core.security import generate_otp
from app.app.crud.otp_crud import otp_sent


class ResendOTPCRUD:

    def __init__(self, db, reset_key):
        self.db = db
        self.reset_key = reset_key

    def resend(self,background_tasks):

        otp_record = self.db.query(EcommerceUserOtp).filter(
            EcommerceUserOtp.reset_key == self.reset_key,
            EcommerceUserOtp.is_used == False
        ).first()

        if not otp_record:
            raise Exception("Invalid reset key")

        user = self.db.query(Users).filter(
            Users.user_id == otp_record.user_id
        ).first()

        if not user:
            raise Exception("User not found")

        email = user.email

        new_otp = generate_otp()

        otp_record.otp = new_otp
        otp_record.expires_at = datetime.now() + timedelta(minutes=5)

        self.db.commit()
        background_tasks.add_task(otp_sent, user.email, new_otp)
        print(new_otp)

        return {
            "timer": 300
        }