# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='day',
            field=models.CharField(max_length=10, choices=[(b'Monday', b'Monday'), (b'Tuesday', b'Tuesday'), (b'Wednesday', b'Wednesday'), (b'Thursday', b'Thursday'), (b'Friday', b'Friday'), (b'Saturday', b'Saturday'), (b'Sunday', b'Sunday')]),
        ),
        migrations.DeleteModel(
            name='Day',
        ),
    ]
