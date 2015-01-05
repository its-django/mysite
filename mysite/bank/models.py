from django.db import models


class Account(models.Model):

    """Simple Bank account with name and money. """

    name = models.CharField(max_length=64)
    money = models.IntegerField()
