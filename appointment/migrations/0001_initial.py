# Generated by Django 4.2.7 on 2023-11-10 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('2023/11/11', '2023/11/11'), ('2023/11/12', '2023/11/12'), ('2023/11/13', '2023/11/13'), ('2023/11/14', '2023/11/14'), ('2023/11/15', '2023/11/15'), ('2023/11/16', '2023/11/16'), ('2023/11/18', '2023/11/18'), ('2023/11/19', '2023/11/19'), ('2023/11/20', '2023/11/20'), ('2023/11/21', '2023/11/21'), ('2023/11/22', '2023/11/22'), ('2023/11/23', '2023/11/23'), ('2023/11/25', '2023/11/25'), ('2023/11/26', '2023/11/26'), ('2023/11/27', '2023/11/27'), ('2023/11/28', '2023/11/28'), ('2023/11/29', '2023/11/29'), ('2023/11/30', '2023/11/30'), ('2023/12/02', '2023/12/02'), ('2023/12/03', '2023/12/03'), ('2023/12/04', '2023/12/04'), ('2023/12/05', '2023/12/05'), ('2023/12/06', '2023/12/06'), ('2023/12/07', '2023/12/07'), ('2023/12/09', '2023/12/09'), ('2023/12/10', '2023/12/10')])),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('time', models.CharField(choices=[('8:00 am', '8:00 am'), ('8:30 am', '8:30 am'), ('9:00 am', '9:00 am'), ('9:30 am', '9:30 am'), ('10:00 am', '10:00 am'), ('10:30 am', '10:30 am'), ('11:00 am', '11:00 am'), ('11:30 am', '11:30 am'), ('12:00 am', '12:00 am'), ('12:30 am', '12:30 am'), ('13:00 am', '13:00 am')])),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
