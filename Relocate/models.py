from django.db import models
from django.contrib.auth.models import User
import geocoder
mapbox_access_token='pk.eyJ1Ijoia2FyYWJvLTIxIiwiYSI6ImNsZmg2ZzZ2bjN0eDkzem80enl1OHdsZ3YifQ.NYQG6cVcf7pa-Ks4Q_jX5A'
# Create your models here.

class Relocate(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    when = models.DateField()
    moving_from = models.CharField(max_length=100)
    moving_to = models.CharField(max_length=100)
  
    def __str__(self): 
        return self.moving_from
class Address(models.Model):
    origin_location = models.TextField()
    destination_location = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    lat2 = models.FloatField(blank=True, null=True)
    long2 = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Geocode first address
        g = geocoder.mapbox(self.origin_location, key=mapbox_access_token)
        g = g.latlng  # returns => [lat, long]
        self.lat = g[0]
        self.long = g[1]

        # Geocode second address if it exists
        if self.destination_location:
            g2 = geocoder.mapbox(self.destination_location, key=mapbox_access_token)
            g2 = g2.latlng  # returns => [lat, long]
            self.lat2 = g2[0]
            self.long2 = g2[1]

        return super(Address, self).save(*args, **kwargs)
            