from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomeUser(AbstractUser):

    address = models.CharField(max_length=200)
    telno = models.CharField(max_length=200)
    