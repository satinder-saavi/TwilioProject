from django.contrib import admin
from django.urls import path, include
from .views import  Home, TwilioSmsView
app_name = 'twilioapp'
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('send-twilio-sms/', TwilioSmsView.as_view(), name='send-twilio-sms'),

]
