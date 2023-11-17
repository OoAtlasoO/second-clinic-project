from django.shortcuts import render
from appointment.models import Appointment
from .forms import PediatricianAppointmentForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


def pediatrician_view(request):
    if request.method == 'POST':
        form = PediatricianAppointmentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            time = cleaned_data['time']
            doctor = cleaned_data['doctor']
            day = cleaned_data['day']
            doctor_appointments = Appointment.objects.filter(doctor=doctor.id)
            day_appointments = doctor_appointments.filter(day=day)
            form.save(commit=False)
            if day_appointments.filter(time=time):
                messages.warning(request, _('this time is reserved'))
            else:
                form.save()
                form = PediatricianAppointmentForm()
                messages.success(request, _('Your appointment has been registered'))

    else:
        form = PediatricianAppointmentForm()

    return render(request, 'pediatrician/pediatrician.html', {
        'form': form,
    })
