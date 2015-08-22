from django.db import models

from core.models import TimeStampedModel

# Create your models here.
class Subscribe(TimeStampedModel):
	email = models.EmailField()
