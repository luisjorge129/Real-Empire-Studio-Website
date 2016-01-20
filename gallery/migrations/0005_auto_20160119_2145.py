# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20160119_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_type',
            field=models.CharField(max_length=16, choices=[(b'Facebook', b'Facebook'), (b'Youtube', b'Youtube')]),
        ),
    ]
