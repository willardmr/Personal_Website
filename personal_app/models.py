from django.db import models

class SimpleModel(models.Model):
    value = models.IntegerField()