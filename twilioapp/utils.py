from twilio.rest import Client
from django.conf import settings


#  ---------------------------------------------------------------
# TwilioMixin
#  ---------------------------------------------------------------
class TwilioMixin:

    _account_sid = settings.TWILIO_ACCOUNT_SID
    _auth_token = settings.TWILIO_AUTH_TOKEN

    client = Client(_account_sid, _auth_token)

    def send_sms(self, text, send_from, send_to):
        send_from = str(send_from)
        send_to = str(send_to)

        message = TwilioMixin.client.messages.create(
            body=text,
            from_=send_from,
            #  messaging_service_sid=settings.MESSAGING_SERVICE_SID,
            to=send_to
        )

        print(message.sid)
        return message
