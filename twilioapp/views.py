from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, UpdateView, ListView
# Create your views here.
class Home(TemplateView):
    '''
    default home view
    '''
    template_name = 'home.html'