from django.shortcuts import render
from .forms import PsychologyAppointmentForm


def psychology_view(request):
    if request.method == 'POST':
        form = PsychologyAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            form = PsychologyAppointmentForm()

    else:
        form = PsychologyAppointmentForm()

    return render(request,'psychology/psychology.html',{
        'form': form,
    })
