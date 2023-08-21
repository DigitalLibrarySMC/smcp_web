from django.db import models

# Create your models here.

class year(models.Model):
    year = models.CharField(max_length=50)

class videos(models.Model):
    year = models.ForeignKey(year)
    occassion = models.CharField(max_length=100,null=True)
    thumbnail = models.ImageField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
