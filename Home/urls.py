from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name="index"),  
    path('services', views.services,name="services"),  
    path('compose/<int:sender_id>/', views.compose_message, name='compose_message'),
    path('inbox/', views.inbox, name='inbox'),
    
    
]