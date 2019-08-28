from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    LocationName = models.CharField(max_length=255)

    LOCATIONID_CHOICES = (
        ('BasundharaGate', 'L1'),
        ('ApoloHospital', 'L2'),
        ('MedehiMart', 'L3'),
        ('DblockMoszid', 'L4'),
    )

    LocationId = models.CharField(max_length=255, choices = LOCATIONID_CHOICES)
