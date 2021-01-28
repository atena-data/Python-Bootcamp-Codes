from twilio.rest import Client

TWILIO_SID = "ACc93427e5a223e5eb0d271674eed00c2a"
TWILIO_AUTH_TOKEN = "a937fabea54d1dab045920eb720e02ec"
TWILIO_VIRTUAL_NUMBER = "+14439032421"
TWILIO_VERIFIED_NUMBER = "+15558675310"

# set up the text notification using twilio API
class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
