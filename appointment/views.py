from django.shortcuts import render
from .forms import AppointmentForm


# Create your views here.
def make_appointment(request):
    if request.method == 'POST':
        appointment_form = AppointmentForm(request.POST)
        if appointment_form.is_valid():
            new_appointment_form=appointment_form.save(commit=False)
            new_appointment_form.user = request.user
            new_appointment_form.save()
    else:
        appointment_form = AppointmentForm()
    return render(request,'appointment/make_appointment.html',{'form':appointment_form})
