from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.pay,name="payment"), 
    path('map/', views.map,name="map"),  
    
    
    
]