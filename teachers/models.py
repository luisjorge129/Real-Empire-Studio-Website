from django.db import models
from django.core.urlresolvers import reverse

from core.models import TimeStampedModel
from core.models import Image

from autoslug import AutoSlugField
from redactor.fields import RedactorField


class Teacher(TimeStampedModel, Image):
    name = models.CharField(max_length=60)
    slug = AutoSlugField(populate_from='name',
                         unique=True, max_length=50)
    biography = RedactorField(verbose_name=u'Text',
                              blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    google_plus = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    course = models.ManyToManyField('teachers.Class',
                                    blank=True)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('teachers:teachers_detail', kwargs={'slug': self.slug})


class Class(TimeStampedModel):
    DAY_OF_THE_WEEK = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    name = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='name',
                         unique=True, max_length=50)
    day = models.CharField(max_length=10,
                           choices=DAY_OF_THE_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


# class Price(TimeStampedModel):
#     title = models.CharField(max_length=40)
#     subtitle = models.CharField(max_length=20)
#     information1 = models.CharField(max_length=40)
#     information2 = models.CharField(max_length=40,
#                                     blank=True)
#     information3 = models.CharField(max_length=40,
#                                     blank=True)
#     information4 = models.CharField(max_length=40,
#                                     blank=True)
#
#     def __unicode__(self):
#         return self.title
