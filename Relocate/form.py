from django import forms
from .models import Relocate,Address


class RelocateForm(forms.ModelForm):
    
    class Meta:
        model = Relocate
        fields = "__all__"  
class AddressForm(forms.ModelForm):
    
    class Meta:
        model = Address
        fields = "__all__"          