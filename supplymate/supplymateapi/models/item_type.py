from django.db import models

class ItemType(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("item_type",)
        verbose_name_plural = ("item_types",)