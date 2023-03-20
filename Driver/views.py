
from django.shortcuts import render
from .models import Driver

# Create your views here.
def displayVihicle(request):
    
    items = Driver.objects.all()
    
    context = {
        "items":items
    }
    
    return render(request,"driver.html",context)
