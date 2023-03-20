from django.urls import path
from . import views

urlpatterns = [
     path("display/",views.displayDriver,name="display"),
      path("show/",views.displayVihicle,name="show"),
]

  
