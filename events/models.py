from django.db import models

from core.models import TimeStampedModel

from autoslug import AutoSlugField


class Event(TimeStampedModel):
	name = models.CharField(max_length=100)
	slug = AutoSlugField(populate_from='name',
						 unique=True, max_length=50)
	# image = models.ImageField()
	time = models.DateTimeField()
	teacher = models.ManyToManyField('teachers.Teacher',
									 blank=True)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return name


class Video(TimeStampedModel):
	youtube_url = models.URLField()
	name = models.CharField(max_length=100, blank=True)
	description = models.TextField(blank=True)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		return name