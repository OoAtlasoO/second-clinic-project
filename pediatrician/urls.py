from django.urls import path
from .views import pediatrician_view
urlpatterns = [
    path('', pediatrician_view, name='pediatrician')
    ]
