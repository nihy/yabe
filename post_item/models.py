from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=75)
	contact_no = models.CharField(max_length=14)
	email = models.EmailField()
	active_items = models.ForeignKey('Item')
	active_bids = models.ForeignKey('Bid')

	def __str__(self):
		return self.name

class Item(models.Model):
	item_name = models.CharField(max_length=75)
	item_desc = models.TextField(max_length=1000)
	sale_price = models.DecimalField(max_digits=8, decimal_places=2)
	post_date = models.DateTimeField('Date Posted ', auto_now_add=True, default=timezone.now())
	for_sale = models.BooleanField(default=False)

def __str__(self):
		return self.item_name

class Bid(models.Model):
	bid_no = models.AutoField(primary_key=True,default=-1)
	bid_amt = models.DecimalField(max_digits=8, decimal_places=2)
	post_date = models.DateTimeField(auto_now_add=True, default=timezone.now())
	accepted = models.BooleanField(default=False)
	item_to_sell = models.ForeignKey('Item',default=0)

def __str__(self):
	return self.bid_no