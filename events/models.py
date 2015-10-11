from django.db import models

from core.models import TimeStampedModel


class Event(TimeStampedModel):
	name = models.CharField(max_length=100)
	image = models.ImageField()
	time = models.DateTimeField()
	teacher = models.ManyToManyField('teachers.Teacher',
									 blank=True)
	status = models.BooleanField(default=True)
