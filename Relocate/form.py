from django import forms
from .models import Relocate


class RelocateForm(forms.ModelForm):
    
    class Meta:
        model = Relocate
        fields = "__all__"  