
from django.shortcuts import render
from .models import Vihicle

# Create your views here.
def displayVihicle(request):
    
    items = Vihicle.objects.all()
    
    context = {
        "items":items
    }
    
    return render(request,"displayVihicle.html",context)
