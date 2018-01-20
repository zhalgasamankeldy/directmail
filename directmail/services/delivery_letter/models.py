from django.db import models

from directmail.audience.models import Audience
from directmail.users.models import User


class DeliveryType(models.Model):
    name = models.CharField(max_length=32)
    price = models.IntegerField(default=0)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Letter(models.Model):
    file = models.FileField()
    delivery_type = models.ForeignKey(DeliveryType, default=1)
    audience = models.ManyToManyField(Audience)
    customer = models.OneToOneField(User, default=1)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
