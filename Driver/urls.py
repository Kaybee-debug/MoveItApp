from django.urls import path
from . import views
app_name = 'Driver'

urlpatterns = [
     # path("display",views.displayDriver,name="display"),
     # path('show/<int:relocate_id>/', views.displayVihicle, name='show'),
     path('show/<int:relocate_id>/', views.displayVihicle, name='show'),
     # path('relocate/<int:relocate_id>/calculate_price/<int:distance>/', views.calculate_price, name='calculate_price', kwargs={'distance': 0}),

     # path('relocate/<int:relocate_id>/calculate_price/<int:distance>/', views.calculate_price, name='calculate_price'),
     path('detail/<int:id>/', views.displayDetail, name='detail'),
    path('Drivers/display/<int:driver_id>/', views.displayDriver, name='displayDriver'),


]

  
