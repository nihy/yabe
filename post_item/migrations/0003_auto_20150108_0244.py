# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post_item', '0002_auto_20150105_0210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='id',
        ),
        migrations.AddField(
            model_name='bid',
            name='bid_no',
            field=models.AutoField(default=-1, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bid',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 8, 2, 44, 22, 417887, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 8, 2, 44, 22, 417278, tzinfo=utc), verbose_name=b'Date Posted ', auto_now_add=True),
            preserve_default=True,
        ),
    ]
