from django.shortcuts import render
from .forms import PediatricianAppointmentForm


def pediatrician_view(request):
    if request.method == 'POST':
        form = PediatricianAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            form = PediatricianAppointmentForm()

    else:
        form = PediatricianAppointmentForm()

    return render(request,'pediatrician/pediatrician.html',{
        'form': form,
    })
