from django.db import models

from django.db import  models


class Items(models.Model):
    item_name = models.CharField(max_length=100)
    item_qty = models.IntegerField(default=1)
    item_sold = models.BooleanField()
    item_entry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name


class Order(models.Model):
    order_no = models.IntegerField(auto_created=True)
    Date_of_order = models.DateTimeField(auto_now_add=True)
    dispached = models.BooleanField()
