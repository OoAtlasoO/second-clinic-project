from django.urls import path
from . import views

urlpatterns = [
    path('', views.DoctorListView.as_view(), name='doctor_list'),
    path('details/<int:pk>', views.doctor_detail_view, name='doctor_detail'),
    path('page/<int:pk>', views.doctor_view, name='doctor_pavilion'),
    path('info/', views.doctor_info, name='doctor_info'),
    path('appointments/', views.doctor_appointment, name='doctor_appointments'),
    path('update/', views.DoctorUpdateInfo.as_view(), name="doctor_update_info")
    ]
