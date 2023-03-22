from django.urls import path
from . import views
from . views import AddressView

urlpatterns = [
     path("bookings",views.new_location,name="bookings"),
     path("schedule",views.new_schedule,name="schedule"),
     path("deliveries/",views.new_deliveries,name="deliveries"),
     path('map/', AddressView.as_view(), name='map'),

     
]
