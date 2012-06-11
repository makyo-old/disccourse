from django.db import models
from disccourse.location.models import Location

class Course(models.Model):
    name = models.CharField(max_length = 250)
    description = models.TextField(blank = True)
    entry_fee = models.DecimalField(max_digits = 5, decimal_places = 2, default = "0.00")
    difficulty = models.IntegerField(default = 0)
    rating = models.IntegerField(default = 0)

class Hole(models.Model):
    course = models.ForeignKey(Course)
    hole_number = models.IntegerField()
    tee = models.ForeignKey(Location)
    hole = models.ForeignKey(Location)
    par = models.IntegerField(default = 1)
    punishment_hole = models.BooleanField(default = False)
    description = models.TextField(blank = True)
    additional_rules = models.TextField(blank = True)
