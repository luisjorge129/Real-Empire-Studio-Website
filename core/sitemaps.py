from django.contrib.sitemaps import Sitemap

from teachers.models import Teacher
from events.models import Event


class HomeSitemap(Sitemap):

    def items(self):
        return [self]

    location = "/"
    changefreq = "monthly"
    priority = "1"


class ContactoSitemap(Sitemap):

    def items(self):
        return [self]

    location = "/contact"
    changefreq = "monthly"
    priority = "1"


class MaestrosSitemap(Sitemap):

    def items(self):
        return [self]

    location = "/maestros"
    changefreq = "monthly"
    priority = "1"


class ClasesSitemap(Sitemap):

    def items(self):
        return [self]

    location = "/clases"
    changefreq = "monthly"
    priority = "1"


class EventosSitemap(Sitemap):

    def items(self):
        return [self]

    location = "/eventos"
    changefreq = "monthly"
    priority = "1"


class VideosSitemap(Sitemap):

    def items(self):
        return [self]

    location = "/videos"
    changefreq = "monthly"
    priority = "1"


class FotosSitemap(Sitemap):

    def items(self):
        return [self]

    location = "/fotos"
    changefreq = "monthly"
    priority = "1"


class MaestrosDetailSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Teacher.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.created_date


class EventosDetailSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Event.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.created_date
