from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class View(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    canvas = models.ImageField()
    
    def __str__(self):
        return self.name
    
    

