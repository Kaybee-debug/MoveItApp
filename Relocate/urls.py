from django.urls import path
from . import views
from . views import AddressView

urlpatterns = [
     path("bookings",views.new_location,name="bookings"),
     path("schedule",views.new_schedule,name="schedule"),
     path("deliveries/<int:user_id>/",views.new_deliveries,name="deliveries"),
     # path("bookings/<pk>/edit/",views.new_schedule,name="schedule"),
    
     path('map/', AddressView.as_view(), name='map'),


]
