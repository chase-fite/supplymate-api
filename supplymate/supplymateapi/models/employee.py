from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from .role import Role


class Employee(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = (F('user.date_joined').asc(nulls_last=True),)
        verbose_name = ("employee",)
        verbose_name_plural = ("employees",)
        