
from django.shortcuts import render
from .models import Driver,Vihicle

# Create your views here.
def displayDriver(request):
    
    items = Driver.objects.all()
    
    context = {
        "items":items
    }
    
    return render(request,"driver.html",context)

def displayVihicle(request):
    
    items = Vihicle.objects.all()
    
    context = {
        "items":items
    }
    
    return render(request,"chooseride.html",context)