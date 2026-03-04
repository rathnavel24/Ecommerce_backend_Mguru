import random 
import smtplib
from email.message import EmailMessage

def OtpSent(user_email):
    otp = ""

    for i in range(6):
        otp+=str(random.randint(0,9))

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('rathnavelpugazh@gmail.com','fyfh ruoi mjvo nson')
    to_mail = user_email

    msg = EmailMessage()

    msg['Subject'] = "OTP Verification"
    msg['From'] = 'rathnavelpugazh@gmail.com'
    msg['To'] = to_mail
    msg.set_content('Your_otp_is: '+otp)

    server.send_message(msg)
    return otp