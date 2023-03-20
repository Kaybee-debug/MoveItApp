from django.shortcuts import render

# Create your views here.
def new_location(request):
    
    return render(request,'relocate.html') 

def new_schedule(request):
    
    return render(request,'schedule.html') 