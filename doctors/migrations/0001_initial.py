# Generated by Django 4.2.7 on 2023-11-10 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciality', models.CharField(choices=[('Dentistry', 'Dentistry'), ('Orthopedic', 'Orthopedic'), ('Psychology', 'Psychology'), ('Oncology', 'Oncology'), ('Pediatrician', 'Pediatrician')])),
                ('service', models.CharField(max_length=300)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkingDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')])),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=50)),
                ('speciality', models.ManyToManyField(related_name='doctors', to='doctors.speciality')),
                ('working_day', models.ManyToManyField(related_name='doctors', to='doctors.workingdays')),
            ],
        ),
    ]
