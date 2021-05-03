from django.shortcuts import render
from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, UpdateView, View, FormView)
from .forms import TwiliioSmsForm
from .utils import TwilioMixin
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse, HttpResponse
from django.conf import settings
#  ---------------------------------------------------------------
# Home
#  ---------------------------------------------------------------
class Home(TemplateView):
    '''
    default home view
    '''
    template_name = 'home.html'

#  ---------------------------------------------------------------
# TwilioSmsView
#  ---------------------------------------------------------------
class TwilioSmsView(FormView, TwilioMixin):
    '''
    Twilio SMS send View
    '''
    form_class = TwiliioSmsForm
    template_name = "twilio_sms_form.html"
    # success_url = reverse_lazy('twilioapp:serial-add')


    def form_valid(self, form, *args, **kwargs):
        sms_text = form.cleaned_data.get('sms_text', None)
        send_to = form.cleaned_data.get('send_to', None)
        send_from = settings.SEND_FROM_NUMBER
        sms_request = self.send_sms(text=sms_text,send_from=send_from,send_to=send_to)
        context = self.get_context_data(**kwargs)
        context['sms_request'] = sms_request
        return render(self.request, 'sms_send_success.html', context)
