from django.db import models

from core.models import TimeStampedModel

from autoslug import AutoSlugField
from redactor.fields import RedactorField

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# class Thumbnail(ImageSpec):
#     processors = [ResizeToFill(100, 50)]
#     format = 'JPEG'
#     options = {'quality': 60}

# source='media/images/'

class Teacher(TimeStampedModel):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name',
                         unique=True, max_length=50)
    image = models.ImageField(upload_to='media')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(100, 100)],
                                     format='JPEG', options={'quality': 60})
    image_small = ImageSpecField(source='image',
                                 processors=[ResizeToFill(160, 160)],
                                 format='JPEG', options={'quality': 60})
    image_medium = ImageSpecField(source='image',
                                  processors=[ResizeToFill(320, 320)],
                                  format='JPEG', options={'quality': 60})
    image_large = ImageSpecField(source='image',
                                 processors=[ResizeToFill(800, 800)],
                                 format='JPEG', options={'quality': 60})
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