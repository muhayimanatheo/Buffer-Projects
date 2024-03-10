from django.db import models

# Create your models here.

class Publications(models.Model):
    names = models.CharField(max_length=200)
    photos = models.ImageField(width_field=200 * 'x', height_field=200 * 'y')
    header = models.CharField(max_length=200)
    text = models.TextField(max_length=200)
    
