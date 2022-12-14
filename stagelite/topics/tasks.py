from __future__ import absolute_import, unicode_literals
from datetime import date, timedelta

from topics.models import Topic

from .celery import app
from celery import shared_task
from topics.lib.import_topics import RedditTopicsParser
from topics.lib.user_interactions import UserInteractions

from stage.models import StageUser


@shared_task()
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


@shared_task()
def import_reddit_topics():
    parser = RedditTopicsParser()
    parser.parse_and_populate_topics()

# Adding STAGE tasks here too for now
@shared_task()
def notify_user_of_new_topic():
    user_interaction = UserInteractions()
    today_topics = Topic.objects.filter(creation_time__gte=(date.today() - timedelta(days=1))).order_by('creation_time')[:3]
    for user in StageUser.objects.all():
        if user.user_email != '':
            user_interaction.notify_user_of_new_topics(user, today_topics)

    return