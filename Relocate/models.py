from django.db import models
import geocoder
mapbox_access_token='pk.eyJ1Ijoia2FyYWJvLTIxIiwiYSI6ImNsZmg2ZzZ2bjN0eDkzem80enl1OHdsZ3YifQ.NYQG6cVcf7pa-Ks4Q_jX5A'
# Create your models here.

class Relocate(models.Model):
    when = models.DateField()
    moving_from= models.CharField(max_length=100)
    moving_to= models.CharField(max_length=100)
  
    def __str__(self): 
        return self.moving_from
class Address(models.Model):
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_access_token)
        g = g.latlng  # returns => [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(Address, self).save(*args, **kwargs)
            