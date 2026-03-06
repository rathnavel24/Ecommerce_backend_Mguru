import random 
import smtplib
from app.app.models.ecommerce_userotp import EcommerceUserOtp
from sqlalchemy.orm import Session
from email.message import EmailMessage
from datetime import datetime, timedelta

def OtpSent(db:Session,user):
    otp = ""

    for i in range(6):
        otp+=str(random.randint(0,9))

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('rathnavelpugazh@gmail.com','fyfh ruoi mjvo nson')
    to_mail = user.email
    expiry_time = datetime.now() + timedelta(minutes=5)

    user_otp = EcommerceUserOtp(
        user_id=user.user_id,
        otp=otp,
        expires_at=expiry_time,
        is_used=False
    )

    db.add(user_otp)
    db.commit()
    db.refresh(user_otp)

    msg = EmailMessage()

    msg['Subject'] = "OTP Verification"
    msg['From'] = 'rathnavelpugazh@gmail.com'
    msg['To'] = to_mail
    msg.set_content('Your_otp_is: '+otp)

    server.send_message(msg)
    server.quit()
    return {"msg": "OTP sent"}
def otp_resent(email,otp):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('rathnavelpugazh@gmail.com','fyfh ruoi mjvo nson')
    to_mail = email

    msg = EmailMessage()
    msg['Subject'] = "OTP Verification"
    msg['From'] = 'rathnavelpugazh@gmail.com'
    msg['To'] = to_mail
    msg.set_content('Your_otp_is: '+otp)

    server.send_message(msg)
    server.quit()
    return {"msg": "OTP sent"}