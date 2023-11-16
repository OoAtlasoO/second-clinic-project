from django.shortcuts import render
from .forms import OrthopedicAppointmentForm


def orthopedic_view(request):
    if request.method == 'POST':
        form = OrthopedicAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            form = OrthopedicAppointmentForm()

    else:
        form = OrthopedicAppointmentForm()

    return render(request,'orthopedic/orthopedic.html',{
        'form': form,
    })
