from appointment.models import Appointment
from django.forms import ModelForm



class DentistryAppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['ordered_service', 'doctor', 'day', 'first_name', 'last_name', 'time']
