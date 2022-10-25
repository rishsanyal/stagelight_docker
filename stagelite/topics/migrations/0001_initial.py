# Generated by Django 3.0.4 on 2022-10-25 03:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateField(auto_now=True)),
                ('creation_time', models.DateField(auto_now_add=True)),
                ('title', models.CharField(help_text='String Title of topic', max_length=1024, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateField(auto_now=True)),
                ('creation_time', models.DateField(auto_now_add=True)),
                ('upvote', models.PositiveIntegerField(default=0)),
                ('downvote', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateField(auto_now=True)),
                ('creation_time', models.DateField(auto_now_add=True)),
                ('submission_entry', models.TextField(help_text='Submission text')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='topics.Topic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='stage.StageUser')),
                ('votes', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_submission_votes', to='topics.Votes')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='topic',
            name='votes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='topic_votes', to='topics.Votes'),
        ),
        migrations.CreateModel(
            name='Competitions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateField(auto_now=True)),
                ('creation_time', models.DateField(auto_now_add=True)),
                ('start_time', models.DateField(auto_now_add=True)),
                ('end_time', models.DateField(default=datetime.datetime(2022, 11, 1, 3, 25, 30, 586737))),
                ('theme', models.CharField(blank=True, max_length=128)),
                ('is_open', models.BooleanField(default=False)),
                ('competition_topics', models.ManyToManyField(null=True, related_name='competition_topics', to='topics.Topic')),
                ('submissions', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='topics.UserSubmission')),
                ('votes', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='competition_votes', to='topics.Votes')),
                ('winner_topic', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='topics.Topic')),
                ('winner_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='stage.StageUser')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]