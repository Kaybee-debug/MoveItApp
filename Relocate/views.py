from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Address

# Create your views here.
def new_location(request):
    
    return render(request,'relocate.html') 

def new_schedule(request):
    
    return render(request,'schedule.html') 

class AddressView(CreateView):

    model = Address
    fields = ['address']
    template_name = 'home.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mapbox_access_token'] = "pk.eyJ1Ijoia2FyYWJvLTIxIiwiYSI6ImNsZmg2ZzZ2bjN0eDkzem80enl1OHdsZ3YifQ.NYQG6cVcf7pa-Ks4Q_jX5A"
        context['addresses'] = Address.objects.all()
        return context