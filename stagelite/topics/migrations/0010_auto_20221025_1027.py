# Generated by Django 3.0.4 on 2022-10-25 10:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0009_auto_20221025_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitions',
            name='end_time',
            field=models.DateField(default=datetime.datetime(2022, 11, 1, 10, 27, 26, 606480)),
        ),
    ]
