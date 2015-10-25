from django.db import models

from core.models import TimeStampedModel
from core.models import Image


class Video(TimeStampedModel):
    name = models.CharField(max_length=100, blank=True)
    youtube_url = models.URLField()
    description = models.TextField(blank=True)
    category = models.ForeignKey('gallery.VideoCategory',
                                 blank=True, null=True)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return name


class Gallery(TimeStampedModel, Image):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey('gallery.GalleryCategory',
                                 blank=True, null=True)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return name


class VideoCategory(TimeStampedModel):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return name


class GalleryCategory(TimeStampedModel):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return name