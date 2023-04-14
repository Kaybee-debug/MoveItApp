
from django.shortcuts import render
from .models import Driver,Vihicle
from django.shortcuts import render, get_object_or_404
from Relocate.models import Relocate


# Create your views here.
def displayDriver(request, driver_id):
    driver = Driver.objects.get(id=driver_id)
    
    context = {
        "driver": driver
    }
    
    return render(request,"driver.html",context)

def displayVihicle(request,relocate_id):
    
    items = Vihicle.objects.all()
    
    context = {
        "items":items,
        "relocate_id": relocate_id
    }
    
    return render(request,"chooseride.html",context)

# def calculate_price(request, relocate_id, distance):
#     relocate = get_object_or_404(Relocate, pk=relocate_id)
#     total_price = relocate.calculate_price(distance)
#     return render(request, 'ridedetail.html', {'total_price': total_price})
def displayDetail(request, id):
    context = {
        'id': id
    }
    return render(request, 'ridedetails.html', context)

