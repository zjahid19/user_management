from send_email import Email
import pyotp

class OtpValidation:
    """This calss is resonsible for oTP validation"""
    def __init__(self,receiver_email):
        self.receiver_email = receiver_email

    def otpvalidation(self):
        """This otp validation methode"""
        receiver_email = self.receiver_email
        totp = pyotp.TOTP('base32secret3232')
        otp = totp.now()
        message_body = f"Otp for your signup process : {otp}"
        email =  Email(receiver_email,message_body)
        email.send_email()
        user_otp=input("Please Enter Your OTP : ")
        return totp.verify(user_otp,valid_window=2)
    