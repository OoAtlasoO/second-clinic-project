
from .views import make_appointment
from django.urls import path, include

urlpatterns = [
    path('make',make_appointment , name='make_appointment')
]
