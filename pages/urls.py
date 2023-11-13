from django.urls import path, include
from .views import HomePageView, AboutUSView, ContactView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutUSView.as_view(), name='about_us'),
    path('contact', ContactView.as_view(), name='contact_us'),
]
