# salon/forms.py

from django import forms
from .models import Booking, Service

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone_number', 'required_services']
        widgets = {
            'required_services': forms.CheckboxSelectMultiple,
        }

