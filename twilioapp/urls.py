from django.contrib import admin
from django.urls import path, include
from .views import  Home
app_name = 'twilioapp'
urlpatterns = [
    path('', Home.as_view(), name='home'),

]
