from appointment.models import Appointment
from django.forms import ModelForm
from doctors.models import Doctor


class DentistryAppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['ordered_service', 'doctor', 'day', 'first_name', 'last_name', 'time']
