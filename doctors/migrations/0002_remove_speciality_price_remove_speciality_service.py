# Generated by Django 4.2.7 on 2023-11-11 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speciality',
            name='price',
        ),
        migrations.RemoveField(
            model_name='speciality',
            name='service',
        ),
    ]