from django.forms import ModelForm
from .models import Comments, Doctor


class DoctorCommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['text']


class CreateDoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ['speciality', 'working_day', 'name', 'last_name', 'phone_number', 'image', 'description']

