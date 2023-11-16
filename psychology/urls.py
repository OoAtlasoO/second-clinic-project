from django.urls import path
from .views import psychology_view
urlpatterns = [
    path('', psychology_view, name='psychology')
    ]
