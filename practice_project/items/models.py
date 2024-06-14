from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    stack = models.IntegerField(default=0)
    category = models.CharField(max_length=100)