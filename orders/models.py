from django.db import models
class Items(models.Model):
    item_name = models.CharField(max_length=100)
    item_qty = models.IntegerField(default=0)
    item_entry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name

    def save_item(self):
        return self.save()


class Order(models.Model):
    item_name = models.ForeignKey(Items,on_delete=models.CASCADE)
    order_no = models.IntegerField(auto_created=True)
    Date_of_order = models.DateTimeField(auto_now_add=True)
    dispached = models.BooleanField(default=False)

    def __str__(self):
        return self.order_no