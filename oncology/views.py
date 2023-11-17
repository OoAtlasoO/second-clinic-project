from django.shortcuts import render, reverse
from .forms import OncologyAppointmentForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from appointment.models import Appointment


def oncology_view(request):
    if request.method == 'POST':
        form = OncologyAppointmentForm(request.POST)
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
                form = OncologyAppointmentForm()
                messages.success(request, _('Your appointment has been registered'))

    else:
        form = OncologyAppointmentForm()

    return render(request,'oncology/oncology.html',{
        'form': form,
    })
