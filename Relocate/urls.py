from django.urls import path
from . import views

urlpatterns = [
     path("bookings/",views.new_location,name="bookings"),
     path("schedule/",views.new_schedule,name="schedule"),
     
]
