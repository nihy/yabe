from django.contrib import admin
from post_item.models import User, Item, Bid

# Register your models here.
admin.site.register(User)
admin.site.register(Item)
admin.site.register(Bid)