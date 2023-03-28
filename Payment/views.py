from django.shortcuts import render,redirect
from .forms import PaymentForm
from .models import Payment

def payment_view(request):
    if request.method == 'POST':
        
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = Payment.objects.create(
                amount=form.cleaned_data['amount'],
                currency=form.cleaned_data['currency'],
                status='Pending'
            )
            # Process payment using payment information from the form
            # Update payment status based on payment processing result
            payment.status = 'Success' # or 'Failed'
            payment.save()
            return redirect('map')
    else:
        form = PaymentForm()
    return render(request, 'payment.html', {'form': form})

def map(request):
    
    return render(request,'map.html') 