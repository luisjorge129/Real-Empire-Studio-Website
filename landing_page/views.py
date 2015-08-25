from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Subscribe


class LandingPage(CreateView):
    template_name = "base 2.html"
    model = Subscribe
    fields = ['email']
    success_url = '/'

