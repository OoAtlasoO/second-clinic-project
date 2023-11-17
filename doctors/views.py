from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from .models import Doctor
from .forms import DoctorCommentForm, CreateDoctorForm
from appointment.models import Appointment
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin


class DoctorListView(generic.ListView):
    model = Doctor
    template_name = 'doctors/doctor_list.html'
    paginate_by = 4


@login_required()
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
            messages.success(request, _('Your Comment has been sent'))

    else:
        comment_form = DoctorCommentForm()
    return render(request, 'doctors/doctor_detail.html', {
        'form': comment_form,
        'comments': doctor_comments,
        'doctor': doctor
    })


def is_member(user):
    return user.groups.filter(name='doctor').exists()


@login_required()
@user_passes_test(is_member)
def doctor_view(request, pk):
    if request.user.id == pk:
        return render(request, 'doctors/doctor_pavilion.html')
    else:
        return redirect('home')


def doctor_info(request):
    if request.method == 'POST':
        form = CreateDoctorForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, _('Your info saved!'))
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


class DoctorUpdateInfo(SuccessMessageMixin,generic.UpdateView):
    model = Doctor
    template_name = 'doctors/doctor_update_info.html'
    fields = ['name', 'last_name', 'phone_number', 'image', 'description']
    success_message = _('Your info successfully saved!!!!')

    def get_object(self, queryset=None):
        obj = get_object_or_404(Doctor, user=self.request.user)
        return obj
