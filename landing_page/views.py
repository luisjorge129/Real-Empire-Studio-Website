from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView


from .models import Subscribe
# from .models import Class


class LandingView(CreateView):
    template_name = "index.html"
    # template_name = "coming_soon/landing.html"
    model = Subscribe
    fields = ['email']
    success_url = 'subscribe/'

class SubscribeView(TemplateView):
    template_name = "subscribe.html"
    # template_name = "coming_soon/landing.html"
    # model = Subscribe
    # fields = ['email']
    # success_url = '/'


class ClassView(TemplateView):
    template_name = "class.html"


class PriceView(TemplateView):
    template_name = "price.html"


class ContactView(TemplateView):
    template_name = "contact.html"
