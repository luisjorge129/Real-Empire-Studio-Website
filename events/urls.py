from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^eventos/$', views.EventsListView.as_view(),
        name='events_list'),
    url(r'^eventos/(?P<slug>[\w-]+)/$', views.EventsDetailView.as_view(),
        name='events_detail'),
    url(r'^api/eventos/$', views.ApiEventList.as_view(),
        name='events_list_api'),
]
