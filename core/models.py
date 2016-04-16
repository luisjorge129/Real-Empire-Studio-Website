from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class TimeStampedModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Image(models.Model):
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

    class Meta:
        abstract = True
