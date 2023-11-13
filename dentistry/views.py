from django.shortcuts import render , get_object_or_404
from .forms import DentistryAppointmentForm
from doctors.models import Doctor, Speciality


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
