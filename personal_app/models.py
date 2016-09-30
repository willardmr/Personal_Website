from django.db import models


class SimpleModel(models.Model):
    """
    Basic model for example purposes
    """
    value = models.IntegerField()
