from django.db import models
from disccourse.location.models import Location
from disccourse.course.models import Hole
from django.contrib.auth.models import User

class Shot(models.Model):
    user = models.ForeignKey(User)
    hole = models.ForeignKey(Hole)
    location = models.ForeignKey(Location)
    timestamp = models.DateTimeField() #not going to set auto_now_add=True because mobile devices may be offline
    final_shot = models.BooleanField(default = False)
