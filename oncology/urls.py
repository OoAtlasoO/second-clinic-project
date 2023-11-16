from django.urls import path
from .views import oncology_view

urlpatterns = [
    path('', oncology_view, name='oncology')
]
