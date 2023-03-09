from django.db import models

class Poi(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(decimal_places=7, max_digits=10)
    longitude = models.DecimalField(decimal_places=7, max_digits=10)
