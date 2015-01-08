# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post_item', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='item_to_sell',
            field=models.ForeignKey(default=0, to='post_item.Item'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bid',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 5, 2, 10, 10, 637451, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 5, 2, 10, 10, 636965, tzinfo=utc), verbose_name=b'Date Posted ', auto_now_add=True),
            preserve_default=True,
        ),
    ]
