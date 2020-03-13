from django.db import models
from .employee import Employee
from .address import Address
from .status import Status
from .item import Item
from .supply_request_item import SupplyRequestItem

class SupplyRequest(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    delivery_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    items = models.ManyToManyField(Item, through=SupplyRequestItem)

    class Meta:
        verbose_name = ("supply_request",)
        verbose_name_plural = ("supply_requests",)