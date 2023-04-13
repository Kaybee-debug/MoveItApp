from django.shortcuts import render,redirect,get_object_or_404

from django.views.generic.edit import CreateView
from .models import Address,Relocate
from .form import RelocateForm
from django.urls import reverse
from django.contrib.auth import get_user_model



# Create your views here.
# def new_location(request):
    
#     return render(request,'relocate.html') 


def new_location(request):
    form = RelocateForm()
    
    if request.method == "POST":
        form = RelocateForm(request.POST)
        if form.is_valid():
            relocate = form.save(commit=False)
            relocate.user = request.user
            relocate.save()
            return redirect(reverse('deliveries', args=[request.user.pk, relocate.pk]))

            
           
    
    context = {
        "form":form
    }
    
   
    return render(request,"relocate.html",context)
def update_location(request, pk):
    location = get_object_or_404(Relocate, pk=pk)
    form = RelocateForm(instance=location)
   
    if request.method == "POST":
        form = RelocateForm(instance=location,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('deliveries', args=[request.user.pk]))
    else:
        form = RelocateForm(instance=location)
    context = {
        "form":form,
        "location":location,
        # "pk":pk,
    }
    
   
    
    return render(request,"schedule.html",context)
# def update(request,pk):
#     listing = Relocate.objects.get(id=pk)
#     form = RelocateForm(instance=listing)
#     if request.method == "POST":
#         form = RelocateForm(request.POST,instance=listing )
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('deliveries', args=[request.user.pk]))
    
    
    
#     context = {
#         "form":form
#     }
   
#     return render(request,"schedule.html",context)

    

def new_deliveries(request, user_id, relocate_id):
    User = get_user_model()
    user = get_object_or_404(User, pk=user_id)
    item = get_object_or_404(Relocate, pk=relocate_id, user=user)

    context = {
        "item": item,
        "user": user,
        "sender_id": user_id,
    }

    return render(request, "deliveries.html", context)


    


# def new_deliveries(request):
#     items = Relocate.objects.all()
    
#     context = {
#         "items":items
#     }
    
   
   
#     return render(request,"deliveries.html",context)

# def new_schedule(request,pk):
#     listing = Relocate.objects.get(id=pk)
#     form = RelocateForm(instance=listing)
#     if request.method == "POST":
#         form = RelocateForm(request.POST,instance=listing , files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("/")
    
    
    
#     context = {
#         "form":form
#     }
   
#     return render(request,"Relocate/schedule.html",context)


# def new_schedule(request):
    
#     return render(request,'schedule.html') 

  

class AddressView(CreateView):

    model = Address
    fields = ['origin_location','destination_location']
    template_name = 'home.html'
    success_url = 'map'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mapbox_access_token'] = "pk.eyJ1Ijoia2FyYWJvLTIxIiwiYSI6ImNsZmg2ZzZ2bjN0eDkzem80enl1OHdsZ3YifQ.NYQG6cVcf7pa-Ks4Q_jX5A"
        context['addresses'] = Address.objects.all()
        return context
    
    