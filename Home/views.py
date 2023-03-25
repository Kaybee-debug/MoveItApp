from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Message
from .forms import MessageForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    
    return render(request,'index.html') 

def services(request):
    
    return render(request,'services.html') 

@login_required
def compose_message(request, sender_id=None):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            messages.success(request, 'Message sent!')
            return redirect('inbox')
    else:
        if sender_id:
            sender = User.objects.get(id=sender_id)
            form = MessageForm(initial={'receiver': sender})
        else:
            form = MessageForm()
    return render(request, 'compose_message.html', {'form': form})

@login_required
def inbox(request):
    messages_received = Message.objects.filter(receiver=request.user)
    return render(request, 'inbox.html', {'messages_received': messages_received})



