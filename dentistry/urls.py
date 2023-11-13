from django.urls import path
from .views import dentistry_view

urlpatterns = [
    path('', dentistry_view, name='dentistry')
]
