from django.db import models

class SupplyRequestItem(models.Model):

    supply_request = models.ForeignKey("SupplyRequest", on_delete=models.DO_NOTHING)
    item = models.ForeignKey("Item", on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=0)

    class Meta:
        verbose_name = ("supply_request_item",)
        verbose_name_plural = ("supply_request_items",)