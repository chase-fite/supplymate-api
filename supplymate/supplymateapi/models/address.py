from django.db import models

class Address(models.Model):

    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=25)
    zip_code = models.CharField(max_length=5)
    

    class Meta:
        verbose_name = ("address",)
        verbose_name_plural = ("addresses",)