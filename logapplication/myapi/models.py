from django.db import models

# Create your models here.
from django.db import models
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    first_movie=models.CharField(max_length=60,null=True)
    latest_movie=models.CharField(max_length=60,null=True)
    def __str__(self):
        return self.name
