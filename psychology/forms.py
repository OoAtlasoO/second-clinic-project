from appointment.models import Appointment
from django.forms import ModelForm, ModelChoiceField
from doctors.models import Doctor, Speciality, Services


class PsychologyAppointmentForm(ModelForm):
    obj = Speciality.objects.get(speciality='Psychology')
    get_object_id = obj.id
    doctor = ModelChoiceField(queryset=Doctor.objects.all().filter(speciality=get_object_id))
    ordered_service = ModelChoiceField(queryset=Services.objects.filter(speciality=get_object_id))

    class Meta:
        model = Appointment
        fields = ['ordered_service', 'doctor', 'day', 'first_name', 'last_name', 'time']
