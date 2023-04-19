from django.db.models import (Model, IntegerField, CharField)


# Create your models here.

class User(Model):
    pass


class Home(Model):
    cost = IntegerField()
    description = CharField(max_length=255)

