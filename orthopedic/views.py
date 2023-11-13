from django.shortcuts import render
from doctors.models import Doctor


def orthopedic_view(request):
    doctors = Doctor.objects.all()
    return render(request, 'orthopedic/orthopedic.html',{
        'doctors': doctors,
    })
