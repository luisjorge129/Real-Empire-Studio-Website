from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from django.conf.urls.i18n import i18n_patterns
from django.views.static import serve

from core.sitemaps import HomeSitemap
from core.sitemaps import ContactoSitemap
from core.sitemaps import EventosSitemap
from core.sitemaps import MaestrosSitemap
from core.sitemaps import ClasesSitemap
from core.sitemaps import VideosSitemap
from core.sitemaps import FotosSitemap
from core.sitemaps import MaestrosDetailSitemap
from core.sitemaps import EventosDetailSitemap

sitemaps = {
    'home': HomeSitemap,
    'contacto': ContactoSitemap,
    'eventos': EventosSitemap,
    'maestros': MaestrosSitemap,
    'clases': ClasesSitemap,
    'videos': VideosSitemap,
    'fotos': FotosSitemap,
    'detail_maestros': MaestrosDetailSitemap,
    'eventos_maestros': EventosDetailSitemap,
}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

    url(r'^robots\.txt$',
        TemplateView.as_view(template_name='robots.txt',
                             content_type='text/plain')),

    url(r'^redactor/', include('redactor.urls')),
]

urlpatterns += i18n_patterns(
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),

    url(r'^', include('landing_page.urls', namespace="landing")),

    url(r'^', include('teachers.urls', namespace="teachers")),

    url(r'^', include('events.urls', namespace="events")),

    url(r'^', include('gallery.urls', namespace="gallery")),
)
