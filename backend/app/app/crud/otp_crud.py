import resend


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



