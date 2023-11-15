from django.contrib import admin
from .forms import CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


# class CustomUserAdmin(UserAdmin):
#     form = CustomUserChangeForm
#     add_form = CustomSignupForm
#     list_display = ['username', 'email', 'age', 'is_staff']
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('age',)}),
#
#     )
#
#     add_fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('age',)}),)
#
#
# admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomUser)
