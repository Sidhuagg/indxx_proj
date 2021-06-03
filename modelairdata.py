from django.db import models

# Create your models here.
class date_time(models.Model):
    last_update = models.DateTimeField()

class Pollutant(date_time):
    poll = models.CharField(max_length=100, null = True)

class airdata(models.Model):
    #id = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    pollutant = models.ForeignKey(Pollutant, on_delete=models.CASCADE)
