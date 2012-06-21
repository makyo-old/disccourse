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
    hole = models.ForeignKey(Location)
    par = models.IntegerField(default = 1)
    punishment_hole = models.BooleanField(default = False)
    description = models.TextField(blank = True)
    additional_rules = models.TextField(blank = True)

class Tee(models.Model):
    hole = models.ForeignKey(Hole)
    location = models.ForeignKey(Location)
    weight = models.IntegerField()

class Hazard(models.Model):
    HAZARD_CHOICES = (
            ('wp', "Water - Pond"),
            ('wl', "Water - Lake"),
            ('wo', "Water - Ocean"),
            ('ws', "Water - Stream"),
            ('wr', "Water - River"),
            ('wc', "Water - Canal"),
            ('bl', "Building - Low"),
            ('bh', "Building - High"),
            ('td', "Tree - Deciduous"),
            ('tp', "Tree - Pine"),
            ('r1', "Rough Terrain - 1 - Manageable"),
            ('r2', "Rough Terrain - 2 - Expert"), 
            ('r2', "Rough Terrain - 3 - Impossible")
            )
    GEOMETRY_CHOICES = (
            ('p', 'Point'),
            ('l', 'Line'),
            ('g', 'Polygon'),
            )
    hole = models.ForeignKey(Hole)
    hazard_type = models.CharField(max_length = 2, choices = HAZARD_CHOICES)
    geometry_type = models.CharField(max_length = 1, choices = GEOMETRY_CHOICES)

class HazardGeometry(models.Model):
    hazard = models.ForeignKey(Hazard)
    location = models.ForeignKey(Location)
    weight = models.IntegerField()
