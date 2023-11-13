from django.contrib import admin
from .models import Doctor, WorkingDays, Speciality, Services, Comments


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkingDays)
class WorkingDayAdmin(admin.ModelAdmin):
    pass


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    pass


@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'user', 'doctor', 'datetime_created', 'is_active']
