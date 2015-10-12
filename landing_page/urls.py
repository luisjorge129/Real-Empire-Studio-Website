from django.conf.urls import url
from .views import LandingView
from .views import PriceView
from .views import ClassView
from .views import ContactView
from .views import SubscribeView


urlpatterns = [
    url(r'^$', LandingView.as_view(), name='landing_page'),
    url(r'^subscribe/$', SubscribeView.as_view(), name='subscribe'),
    url(r'^precios/$', PriceView.as_view(), name='price'),
    url(r'^clases/$', ClassView.as_view(), name='class'),
    url(r'^contacto/$', ContactView.as_view(), name='contact'),
]
