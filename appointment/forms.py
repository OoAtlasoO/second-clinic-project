from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['day', 'first_name', 'last_name', 'time', 'doctor']
