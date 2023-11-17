from django.shortcuts import render
from appointment.models import Appointment
from .forms import PsychologyAppointmentForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


def psychology_view(request):
    if request.method == 'POST':
        form = PsychologyAppointmentForm(request.POST)
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
            if day_appointments.count() >= 11:
                messages.warning(request, _('this day visit is full!'))
            else:
                form.save()
                form = PsychologyAppointmentForm()
                messages.success(request, _('Your appointment has been registered'))

    else:
        form = PsychologyAppointmentForm()

    return render(request, 'psychology/psychology.html', {
        'form': form,
    })
