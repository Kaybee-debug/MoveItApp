from django import forms
from .models import Relocate,Address



    
class RelocateForm(forms.ModelForm):
    class Meta:
        model = Relocate
        fields = ['when', 'moving_from', 'moving_to']
        widgets = {
            'when': forms.DateInput(attrs={'type': 'date'}),
            'moving_from': forms.TextInput(attrs={'placeholder': 'Moving from'}),
            'moving_to': forms.TextInput(attrs={'placeholder': 'Moving to'})
        } 
class AddressForm(forms.ModelForm):
    
    class Meta:
        model = Address
        fields = "__all__"          