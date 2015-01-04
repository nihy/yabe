# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bid_amt', models.DecimalField(max_digits=8, decimal_places=2)),
                ('post_date', models.DateTimeField(default=datetime.datetime(2015, 1, 4, 23, 17, 53, 943959, tzinfo=utc), auto_now_add=True)),
                ('accepted', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=75)),
                ('item_desc', models.TextField(max_length=1000)),
                ('sale_price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('post_date', models.DateTimeField(default=datetime.datetime(2015, 1, 4, 23, 17, 53, 943025, tzinfo=utc), verbose_name=b'Date Posted ', auto_now_add=True)),
                ('for_sale', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75)),
                ('contact_no', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=75)),
                ('active_bids', models.ForeignKey(to='post_item.Bid')),
                ('active_items', models.ForeignKey(to='post_item.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
