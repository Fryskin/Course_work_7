# Generated by Django 4.2.4 on 2023-09-28 17:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useful_habits', '0007_alter_usefulhabit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usefulhabit',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 9, 28, 17, 38, 34, 741322, tzinfo=datetime.timezone.utc), verbose_name='time'),
        ),
    ]
