# Generated by Django 3.2.16 on 2022-12-14 04:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0015_auto_20221026_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitions',
            name='creation_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='competitions',
            name='last_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='topic',
            name='creation_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='topic',
            name='last_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='usersubmission',
            name='creation_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='usersubmission',
            name='last_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='votes',
            name='creation_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='votes',
            name='last_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
