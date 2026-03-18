
import smtplib

from sqlalchemy.orm import Session
from email.message import EmailMessage

def otp_sent(email,otp):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('rathnavelwork@gmail.com','sjxo fcnt jiww crtm')
    to_mail = email

    msg = EmailMessage()
    msg['Subject'] = "OTP Verification"
    msg['From'] = 'rathnavelwork@gmail.com'
    msg['To'] = to_mail
    msg.set_content('Your_otp_is: '+otp)

    server.send_message(msg)
    server.quit()
    return {"msg": "OTP sent"}