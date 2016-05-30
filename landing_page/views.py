from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

from .models import Subscribe


class LandingView(CreateView):
    template_name = "index.html"
    model = Subscribe
    fields = ['email']
    success_url = 'subscribe/'


class SubscribeView(TemplateView):
    template_name = "subscribe.html"


class PriceView(TemplateView):
    template_name = "price.html"


class ContactView(TemplateView):
    template_name = "contact.html"
