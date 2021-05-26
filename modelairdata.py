from django.db import models

# Create your models here.
class date_time(models.Model):
    last_update = models.CharField(max_length=100)



class Pollutant(date_time):
    pollutant_id = models.CharField(max_length=50)
    pollutant_min = models.IntegerField()
    pollutant_max = models.IntegerField()
    pollutant_avg = models.IntegerField()

class airdata(models.Model):
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    station = models.CharField(max_length=100)
    pollutant = models.ForeignKey(Pollutant, on_delete=models.CASCADE)
