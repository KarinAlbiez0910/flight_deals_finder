import os
from twilio.rest import Client

class NotificationManager:
    def __init__(self):
        self.account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
        self.auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

    def send_message(self, body):
        client = Client(self.account_sid, self.auth_token)

        message = client.messages \
            .create(
            body=body,
            from_=os.environ.get("TWILIO_PHONE_NUMBER"),
            to=os.environ.get('MY_PHONE_NUMBER')
        )

        print(message.status)
