# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_auto_20151116_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='course',
            field=models.ManyToManyField(to='teachers.Class', blank=True),
        ),
    ]
