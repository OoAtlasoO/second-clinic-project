from django.shortcuts import render
from .forms import DentistryAppointmentForm


def dentistry_view(request):
    if request.method == 'POST':
        form = DentistryAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            form = DentistryAppointmentForm()

    else:
        form = DentistryAppointmentForm()

    return render(request,'dentistry/dentistry.html',{
        'form': form,
    })
