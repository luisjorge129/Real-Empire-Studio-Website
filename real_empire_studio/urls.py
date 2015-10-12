from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('landing_page.urls', namespace="landing")),
    url(r'^', include('teachers.urls', namespace="teachers")),
    url(r'^', include('events.urls', namespace="events")),
]
