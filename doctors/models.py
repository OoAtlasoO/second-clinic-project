from django.db import models

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
    speciality = models.ForeignKey(Speciality, related_name='doctors', on_delete=models.CASCADE,null=True)
    working_day = models.CharField(choices=WEEK_DAYS, blank=True, max_length=50)
    second_working_day = models.CharField(choices=WEEK_DAYS, blank=True, max_length=50)
    third_working_day = models.CharField(choices=WEEK_DAYS, blank=True, max_length=50)
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=50)
    image = models.ImageField(upload_to='doctor_images/', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):

        return f'{self.name} {self.last_name} : {self.speciality}'

    def get_working_days(self):
        days = []
        days.append(self.working_day)
        days.append(self.second_working_day)
        days.append(self.third_working_day)
        return days


class Services(models.Model):
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    service = models.CharField(max_length=150)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.speciality} - {self.service} : {self.price}'



