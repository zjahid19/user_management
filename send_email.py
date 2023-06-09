""" This module for sending an email"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Email:
    """This class is responsible for sending verification otp"""
    def __init__(self,receiver_email,message_body):
        self.sender_email = 'Youremail@gmail.com'
        self.receiver_email = 'receiver_email@gmail.com'
        self.subject = 'Signup OTP for Application'
        self.body = message_body
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 587  # TLS Port
        self.username = 'Youremail@gmail.com'
        self.password = 'password'
        self.receiver_email = receiver_email
    def send_email(self):
        """This method is responsible for sending an email"""
        try:
            message = MIMEMultipart()
            message['From'] = self.sender_email
            message['To'] = self.receiver_email
            message['Subject'] = self.subject
            message.attach(MIMEText(self.body, 'plain'))
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.username, self.password)
            server.sendmail(self.sender_email, self.receiver_email, message.as_string())
            print(f'OTP sent to Email address {self.receiver_email} sent successfully!')
        except Exception as email_exc:
            print('An error occurred while sending the email:', str(email_exc))
        finally:
            server.quit()
