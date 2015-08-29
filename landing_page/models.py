from django.db import models

from core.models import TimeStampedModel


# Create your models here.
class Subscribe(TimeStampedModel):
    email = models.EmailField()


# class Styles(TimeStampedModel):
#     name = models.CharField(max_length=255)


# # Create your models here.
# class Class(TimeStampedModel):
#     title = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     fechaEmpieza = models.DateTimeField()
#     fechaTermina = models.DateTimeField(auto_now=True)
#     todaLaSemana = models.BooleanField()
#     email = models.EmailField()


# # Create your models here.
# class Teachers(TimeStampedModel):
#     name = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     style = models.models.ManyToManyField(Styles, verbose_name="list of styles")
#     class_name = models.ManyToManyField(Class, verbose_name="list of classes")
