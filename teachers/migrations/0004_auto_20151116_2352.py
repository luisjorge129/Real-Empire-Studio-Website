# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_auto_20151116_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='biography',
            field=redactor.fields.RedactorField(verbose_name='Text', blank=True),
        ),
    ]
