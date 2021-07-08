from django.db import models
class Items(models.Model):
    item_image = models.ImageField(null=True)
    item_name = models.CharField(max_length=100)
    item_qty = models.IntegerField(default=0)
    item_entry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name

    def save_item(self):
        return self.save()


class Order(models.Model):
    Item_id = models.ForeignKey(Items,on_delete=models.CASCADE)
    Date_of_order = models.DateTimeField(auto_now_add=True)
    dispached = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    def save_order(self):
        return self.save()