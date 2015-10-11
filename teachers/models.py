from django.db import models

from core.models import TimeStampedModel


class Teacher(TimeStampedModel):
	name = models.CharField(max_length=100)
	image = models.ImageField()
	facebook = models.URLField(blank=True)
	twitter = models.URLField(blank=True)
	instagram = models.URLField(blank=True)
	course = models.ManyToManyField("teachers.Course")
	status = models.BooleanField(default=True)

class Course(TimeStampedModel):
	name = models.CharField(max_length=150)
	time = models.DateTimeField()
	status = models.BooleanField(default=True)
