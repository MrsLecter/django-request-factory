import datetime
from django.db import models

class Basket(models.Model):
    id = models.AutoField(primary_key=True, unique=True, auto_created=True, null=False)
    name = models.CharField(null=False, max_length=200)
    description = models.CharField(null=False, max_length=500)
    price = models.IntegerField(null=False)
    presence = models.BooleanField(null=False)
    created = models.DateTimeField(null=False, default=datetime.datetime.now)