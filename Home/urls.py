from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),  
    path('services', views.services,name="services"),  
    path('chat', views.chat,name="chat"), 
    
    
]