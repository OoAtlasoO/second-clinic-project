from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
WEEK_DAYS = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)
SPECIALITY_CHOICES = [
    ('Dentistry', 'Dentistry'),
    ('Orthopedic', 'Orthopedic'),
    ('Psychology', 'Psychology'),
    ('Oncology', 'Oncology'),
    ('Pediatrician', 'Pediatrician'),
]


class WorkingDays(models.Model):
    day = models.CharField(choices=WEEK_DAYS)

    def __str__(self):
        return self.day


class Speciality(models.Model):
    speciality = models.CharField(choices=SPECIALITY_CHOICES)

    def __str__(self):
        return f'{self.speciality}'


class Doctor(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True, related_name='doctor')
    speciality = models.ForeignKey(Speciality, related_name='doctors', on_delete=models.CASCADE, null=True)
    working_day = models.CharField(choices=WEEK_DAYS, blank=True, max_length=50)
    second_working_day = models.CharField(choices=WEEK_DAYS, blank=True, max_length=50)
    third_working_day = models.CharField(choices=WEEK_DAYS, blank=True, max_length=50)
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=50)
    image = models.ImageField(upload_to='doctor_images/', blank=True)
    description = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('doctor_detail', args=[self.id])

    def __str__(self):

        return f'{self.name} {self.last_name} : {self.speciality}'


class Services(models.Model):
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    service = models.CharField(max_length=150)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.speciality} - {self.service} : {self.price}'


class Comments(models.Model):
    text = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name= 'comments')
    datetime_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.text
