from django.urls import path
from .views import orthopedic_view
urlpatterns = [
    path('', orthopedic_view, name='orthopedic')
    ]
