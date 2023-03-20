from django.db import models

# Create your models here.

class Relocate(models.Model):
    when = models.DateField()
    moving_from= models.CharField(max_length=100)
    moving_to= models.CharField(max_length=100)
  
    def __str__(self): 
        return self.moving_from