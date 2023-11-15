from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from .models import Doctor
from .forms import DoctorCommentForm, CreateDoctorForm
from appointment.models import Appointment
from django.contrib.auth import get_user_model


class DoctorListView(generic.ListView):
    model = Doctor
    template_name = 'doctors/doctor_list.html'


def doctor_detail_view(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    doctor_comments = doctor.comments.all()
    if request.method == 'POST':
        comment_form = DoctorCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment_form = comment_form.save(commit=False)
            new_comment_form.user = request.user
            new_comment_form.doctor = doctor
            new_comment_form.save()

    else:
        comment_form = DoctorCommentForm()
    return render(request, 'doctors/doctor_detail.html', {
        'form': comment_form,
        'comments': doctor_comments,
        'doctor': doctor
    })


def doctor_view(request, pk):
    return render(request, 'doctors/doctor_pavilion.html')


def doctor_info(request):
    if request.method == 'POST':
        form = CreateDoctorForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('doctor_pavilion', pk=request.user.id)
    else:
        form = CreateDoctorForm()
    return render(request, 'doctors/doctor_info.html', {'form': form})


def doctor_appointment(request):
    doctor = get_object_or_404(Doctor, name=request.user.first_name)
    appointments = Appointment.objects.filter(doctor=doctor)
    return render(request, 'doctors/doctor_appointment_list.html', {
        'doctor': doctor,
        'appointments': appointments,
    })
