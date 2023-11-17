from django.db import models
from datetime import datetime, timedelta
from doctors.models import Services, Doctor
from django.utils.translation import gettext_lazy as _


def get_valid_days(days=31):
    now = datetime.now()
    today = now.date()
    valid_days = []
    for i in range (0,days):
        next_day = today+timedelta(days=i)
        next_day_name = next_day.strftime('%A')
        if next_day_name == 'Friday':
            pass
        else:
            valid_days.append((next_day.strftime('%Y/%m/%d'),next_day.strftime('%Y/%m/%d')))
    return valid_days


TIME_CHOICES = [
    ('8:00 am', '8:00 am'),
    ('8:30 am', '8:30 am'),
    ('9:00 am', '9:00 am'),
    ('9:30 am', '9:30 am'),
    ('10:00 am', '10:00 am'),
    ('10:30 am', '10:30 am'),
    ('11:00 am', '11:00 am'),
    ('11:30 am', '11:30 am'),
    ('12:00 am', '12:00 am'),
    ('12:30 am', '12:30 am'),
    ('13:00 am', '13:00 am'),

]


class Appointment(models.Model):
    ordered_service = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name=_('ordered service'))
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments', verbose_name=_('doctor'))
    day = models.CharField(choices=get_valid_days(31), verbose_name=_('day'))
    first_name = models.CharField(max_length=150, verbose_name=_('first name'))
    last_name = models.CharField(max_length=150, verbose_name=_('last name'))
    time = models.CharField(choices=TIME_CHOICES, verbose_name=_('time'))
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.doctor}: {self.day}--{self.time}'

