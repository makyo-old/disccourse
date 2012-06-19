from django.contrib.gis.db import models

class Location(models.Model):
    accuracy = models.DecimalField(max_digits = 8, decimal_places = 4)
    heading = models.DecimalField(max_digits = 8, decimal_places = 4)
    speed = models.DecimalField(max_digits = 8, decimal_places = 4)
    altitude = models.DecimalField(max_digits = 8, decimal_paces = 4)
    altitude_accuracy = models.IntegerField(max_digits = 8, decimal_places = 4)
    point = models.PointField()
    objects = models.GeoManager()
