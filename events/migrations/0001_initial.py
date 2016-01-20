# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to=b'media')),
                ('name', models.CharField(max_length=100)),
                ('description', redactor.fields.RedactorField(verbose_name='Text', blank=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from=b'name', unique=True, editable=False)),
                ('time', models.DateTimeField()),
                ('status', models.BooleanField(default=True)),
                ('facebook', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('google_plus', models.URLField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
