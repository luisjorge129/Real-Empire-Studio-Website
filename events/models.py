from django.db import models

from autoslug import AutoSlugField

from core.models import TimeStampedModel
from core.models import Image


class Event(TimeStampedModel, Image):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='name',
                         unique=True, max_length=50)
    time = models.DateTimeField()
    teacher = models.ManyToManyField('teachers.Teacher',
                                     blank=True)
    status = models.BooleanField(default=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    google_plus = models.URLField(blank=True)

    def __unicode__(self):
        return self.name
