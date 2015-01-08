# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post_item', '0003_auto_20150108_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 8, 2, 57, 9, 610730, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 8, 2, 57, 9, 610222, tzinfo=utc), verbose_name=b'Date Posted ', auto_now_add=True),
            preserve_default=True,
        ),
    ]
