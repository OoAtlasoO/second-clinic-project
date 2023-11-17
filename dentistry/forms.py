from appointment.models import Appointment
from django.forms import ModelForm, ModelChoiceField
from doctors.models import Doctor, Speciality, Services
from django.utils.translation import gettext_lazy as _


class DentistryAppointmentForm(ModelForm):
    obj = Speciality.objects.get(speciality='Dentistry')
    get_object_id = obj.id
    doctor = ModelChoiceField(queryset=Doctor.objects.all().filter(speciality=get_object_id), label=_('doctor'))
    ordered_service = ModelChoiceField(
        queryset=Services.objects.filter(speciality=get_object_id),
        label=_('ordered service'))

    class Meta:
        model = Appointment
        fields = ['ordered_service', 'doctor', 'day', 'first_name', 'last_name', 'time']
