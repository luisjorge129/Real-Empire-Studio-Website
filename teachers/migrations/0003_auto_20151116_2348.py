# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20151101_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
