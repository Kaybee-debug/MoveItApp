
    
from django import forms

class PaymentForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    currency = forms.CharField(max_length=3)
    card_number = forms.CharField(widget=forms.TextInput(attrs={'style': 'width: 55vw;'}))
    cvv = forms.CharField(widget=forms.PasswordInput(attrs={'style': 'width: 20vw; margin-left: auto;'}), max_length=3)
    expiry_date = forms.DateField()
    payment_method = forms.ChoiceField(choices=[('', '--Select--'), ('visa', 'Visa'), ('mastercard', 'Mastercard'), ('paypal', 'PayPal')], required=True)    