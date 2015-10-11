from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('landing_page.urls')),
    url(r'^', include('teachers.urls')),
    url(r'^', include('events.urls')),
]
