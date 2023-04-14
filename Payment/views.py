from django.shortcuts import render,redirect
from .forms import PaymentForm
from .models import Payment
from django.http import HttpResponse
import twilio.twiml.voice_response

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
# def make_phone_call(request):
#     phone_number = request.POST.get('phone_number')

#     # Generate TwiML response to initiate a phone call
#     twiml_response = twilio.twiml.voice_response.VoiceResponse()
#     twiml_response.dial(phone_number)

#     # Return the TwiML response as an HttpResponse
#     return HttpResponse(str(twiml_response))
def make_phone_call(request):
    phone_number = request.POST.get('phone_number')

    # Generate TwiML response to initiate a phone call
    twiml_response = twilio.twiml.voice_response.VoiceResponse()
    twiml_response.dial(phone_number)

    # Return the TwiML response as an HttpResponse
    return HttpResponse(str(twiml_response))