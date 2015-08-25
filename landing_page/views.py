from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Subscribe


class LandingPage(CreateView):
    template_name = "index.html"
    # template_name = "coming_soon/landing.html"
    model = Subscribe
    fields = ['email']
    success_url = '/'

