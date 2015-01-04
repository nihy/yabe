from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=75)
	contact_no = models.CharField(max_length=14)
	email = models.EmailField()
	active_items = models.ForeignKey('Item')
	active_bids = models.ForeignKey('Bid')

class Item(models.Model):
	item_name = models.CharField(max_length=75)
	item_desc = models.TextField(max_length=1000)
	sale_price = models.DecimalField(max_digits=8, decimal_places=2)
	post_date = models.DateTimeField('Date Posted ', auto_now_add=True, default=timezone.now())
	for_sale = models.BooleanField(default=False)

class Bid(models.Model):
	bid_amt = models.DecimalField(max_digits=8, decimal_places=2)
	post_date = models.DateTimeField(auto_now_add=True, default=timezone.now())
	accepted = models.BooleanField(default=False)