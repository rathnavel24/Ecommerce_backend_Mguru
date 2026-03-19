
#import smtplib
import resend
#from sqlalchemy.orm import Session
#from email.message import EmailMessage

def otp_sent(email,otp):

    resend.api_key = "re_MNdtr3Qk_AZvnz2XZBLu6USSUdko77uPC"

    try:
        r = resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": email,
        "subject": "OTP Verification",
        "html": 'Your_otp_is: '+otp
        })

        return  {
            "msg": "OTP sent"
            }
    except Exception as e:
        return e
    
    '''
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
    '''



