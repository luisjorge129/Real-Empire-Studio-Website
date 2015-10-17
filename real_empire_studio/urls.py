from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^', include('landing_page.urls', namespace="landing")),
    url(r'^', include('teachers.urls', namespace="teachers")),
    url(r'^', include('events.urls', namespace="events")),
]
