from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request,'index.html') 

def services(request):
    
    return render(request,'services.html') 

def chat(request):
    
    return render(request,'chat.html') 




