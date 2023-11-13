from django.forms import ModelForm
from .models import Comments


class DoctorCommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
