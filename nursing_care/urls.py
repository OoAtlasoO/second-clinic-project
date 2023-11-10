from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='nursing_care/nursing_care.html'), name='nursing_care'),
]
