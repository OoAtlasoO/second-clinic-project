from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model


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
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    day = models.CharField(choices=get_valid_days(31))
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    time = models.CharField(choices=TIME_CHOICES)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

