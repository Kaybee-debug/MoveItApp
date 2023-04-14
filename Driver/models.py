from django.db import models

# Create your models here.

class Driver(models.Model):
    driver_name = models.CharField(max_length=100)
    car_registration= models.CharField(max_length=100)
    model= models.CharField(max_length=100)
    image = models.ImageField()

  
    def __str__(self): 
        return self.driver_name  
    

class Vihicle(models.Model):
    Trailer ='Trailer'
    Bakkie ='Bakkie'
    Truck ='Truck'
    transportationChoice = [
        (Trailer,'Trailer'),
        (Bakkie,'Bakkie'),
        (Truck ,'Truck')
    ] 
    transportation = models.CharField(max_length=7,choices=transportationChoice, default=Trailer )  
    price = models.DecimalField(max_digits=6,decimal_places=2)
    weight = models.IntegerField()
    car_registration= models.ForeignKey(Driver,on_delete=models.PROTECT)
    image = models.ImageField()

    
    
    def __str__(self): 
        return self.transportation


    
