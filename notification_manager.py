import os
from twilio.rest import Client
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.ACC_SID = os.getenv('ACC_SID')
        self.AUTH_TOKEN = os.getenv('AUTH_TOKEN')
        self.FROM_PHONE = os.getenv('FROM_PHONE')
        self.TO_PHONE = os.getenv('TO_PHONE')
        self.CLIENT = Client(self.ACC_SID, self.AUTH_TOKEN)
        self.my_google_email = os.getenv('my_google_email')
        self.google_password = os.getenv('google_password')

    def send_alert(self,message):
        """Sends given message to your phone number"""

        message = self.CLIENT.messages.create(
            body=message,
            from_=self.FROM_PHONE,
            to=self.TO_PHONE,
        )

    def send_mails(self,email_list,message):
        """Sends mail to your email address"""

        for email in email_list:
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=self.my_google_email, password=self.google_password)
                connection.sendmail(from_addr=self.my_google_email, to_addrs=email,
                                    msg=message)