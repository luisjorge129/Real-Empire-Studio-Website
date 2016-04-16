from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.LandingView.as_view(), name='landing_page'),
    url(r'^subscribe/$', views.SubscribeView.as_view(), name='subscribe'),

    url(r'^contacto/$', views.ContactView.as_view(), name='contact'),
]
