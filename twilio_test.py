from twilio.rest import Client
from django.conf import settings
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TwilioProject.settings')
django.setup()

#  ---------------------------------------------------------------
# test_twilio
#  ---------------------------------------------------------------
def test_twilio():
    """
    
    In trail version to must be in the verified number list
    https://www.twilio.com/console/phone-numbers/verified

    and also to send in another geo location it should be nebaled via
    https://www.twilio.com/console/sms/settings/geo-permissions

    also from should be from https://www.twilio.com/console/phone-numbers/incoming


    """
    print("=======================")
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    messaging_service = settings.MESSAGING_SERVICE_SID
    SEND_FROM = settings.SEND_FROM_NUMBER
    SEND_TO = settings.SEND_TO_NUMBER
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                 body="\n Join Earth's mightiest heroes. Like Kevin Bacon.",
                 from_=SEND_FROM,
                #  messaging_service_sid=messaging_service,  
                 to=SEND_TO
             )

    print(message)
    print(message.sid)
    print("=======================")


if __name__ == '__main__':
    test_twilio()