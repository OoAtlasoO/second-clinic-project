from django.urls import path
from . import views

urlpatterns = [
    path('', views.DoctorListView.as_view(), name='doctor_list'),
    path('details/<int:pk>', views.DoctorDetailView.as_view(), name='doctor_detail')
    ]
