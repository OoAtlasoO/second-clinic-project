from django.shortcuts import render
from .forms import OncologyAppointmentForm


def oncology_view(request):
    if request.method == 'POST':
        form = OncologyAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            form = OncologyAppointmentForm()

    else:
        form = OncologyAppointmentForm()

    return render(request,'oncology/oncology.html',{
        'form': form,
    })
