from django.db import models

from core.models import TimeStampedModel
from core.models import Image

from autoslug import AutoSlugField
from redactor.fields import RedactorField


class Teacher(TimeStampedModel, Image):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name',
                         unique=True, max_length=50)
    biography = RedactorField(verbose_name=u'Text')
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    google_plus = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    course = models.ManyToManyField("teachers.Course")
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

class Course(TimeStampedModel):
    name = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='name',
                         unique=True, max_length=50)
    time = models.DateTimeField()
    status = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name