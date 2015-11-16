from django.db import models

from core.models import TimeStampedModel
from core.models import Image


class Video(TimeStampedModel):
    name = models.CharField(max_length=40, blank=True)
    youtube_id = models.CharField(max_length=20)
    description = models.CharField(blank=True, max_length=50)
    category = models.ManyToManyField('gallery.VideoCategory',
                                      blank=True)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Gallery(TimeStampedModel, Image):
    name = models.CharField(max_length=40, blank=True)
    description = models.TextField(blank=True, max_length=50)
    category = models.ManyToManyField('gallery.GalleryCategory',
                                      blank=True)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class VideoCategory(TimeStampedModel):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name


class GalleryCategory(TimeStampedModel):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name