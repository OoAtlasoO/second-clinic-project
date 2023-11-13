from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Doctor
from .forms import DoctorCommentForm


class DoctorListView(generic.ListView):
    model = Doctor
    template_name = 'doctors/doctor_list.html'


def doctor_detail_view(request,pk):
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


