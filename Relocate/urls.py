from django.urls import path
from . import views
from . views import AddressView

urlpatterns = [
     path("bookings",views.new_location,name="bookings"),
     path('edit_location/<int:relocate_id>/',views.edit_location, name='edit_location'),

     path("locations/<int:pk>/",views.update_location,name="update_location"),
     # path("deliveries/<int:user_id>/",views.new_deliveries,name="deliveries"),
      path("deliveries/<int:user_id>/<int:relocate_id>/", views.new_deliveries, name="deliveries"),
     # path("bookings/<pk>/edit/",views.new_schedule,name="schedule"),
    
     path('map/', AddressView.as_view(), name='map'),


]
