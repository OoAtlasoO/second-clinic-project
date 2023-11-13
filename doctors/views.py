from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Doctor


class DoctorListView(generic.ListView):
    model = Doctor
    template_name = 'doctors/doctor_list.html'


class DoctorDetailView(generic.DetailView):
    model = Doctor
    template_name = 'doctors/doctor_detail.html'

