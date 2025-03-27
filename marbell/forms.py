from django import forms
import re
from .models import *
from django.core.exceptions import ValidationError

class BidCreation(forms.ModelForm):
    class Meta:
        model = Bid
        fields = (
            'first_name',
            'last_name',
            'email_address',
            'phone_number',
            'message' 
        )

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email_address': forms.EmailInput(attrs={'class':'form-control'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control'}),
            'message': forms.Textarea(attrs={'class':'form-control'})
        }
