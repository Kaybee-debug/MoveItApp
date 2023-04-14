from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.payment_view,name="payment"), 
    path('map', views.map,name="map"),  
    path('make_phone_call/', views.make_phone_call, name='make_phone_call'),
    
    
    
]