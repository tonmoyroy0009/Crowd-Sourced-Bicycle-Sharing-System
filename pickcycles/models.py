from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pickcycle(models.Model):
    LocationId = models.CharField(max_length=255)
    Picker = models.ForeignKey(User, on_delete=models.CASCADE)