from appointment.models import Appointment
from django.forms import ModelForm


class PediatricianAppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['ordered_service', 'doctor', 'day', 'first_name', 'last_name', 'time']
