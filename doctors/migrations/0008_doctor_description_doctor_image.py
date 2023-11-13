# Generated by Django 4.2.7 on 2023-11-12 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0007_doctor_second_working_day_doctor_third_working_day_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, upload_to='doctor_images/'),
        ),
    ]
