from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from .role import Role


class Employee(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("employee",)
        verbose_name_plural = ("employees",)
        