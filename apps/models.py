from django.db.models import (Model, IntegerField, CharField)
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(Model):
    pass


class Home(Model):
    cost = IntegerField()
    description = CharField(max_length=255)


class Users(AbstractUser):
    ...
