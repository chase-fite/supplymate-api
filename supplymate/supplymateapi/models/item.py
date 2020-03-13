from django.db import models
from .item_type import ItemType
from .address import Address

class Item(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    serial_number = models.CharField(max_length=50)
    stock = models.IntegerField()
    quantity = models.IntegerField()
    item_type = models.ForeignKey(ItemType, on_delete=models.DO_NOTHING)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    storage_location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        # ordering = ("name",)
        verbose_name = ("item",)
        verbose_name_plural = ("items",)
