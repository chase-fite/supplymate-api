from django.db import models

class Role(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("role",)
        verbose_name_plural = ("roles",)