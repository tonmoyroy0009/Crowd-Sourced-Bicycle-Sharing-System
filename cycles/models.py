from django.db import models
from django.contrib.auth.models import User

# Create your models here.
 
class Cycle(models.Model):

    OwnerId = models.ForeignKey(User, on_delete=models.CASCADE)
    CycleName = models.CharField(max_length=255)
    CycleModelName = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

