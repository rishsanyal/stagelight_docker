from __future__ import absolute_import, unicode_literals
from django.conf import settings

# import settings
# from django.conf import CELERY_RESULT_BACKEND, CELERY_BROKER_URL
from stagelite.settings import CELERY_RESULT_BACKEND, CELERY_BROKER_URL

from celery import Celery

# Result backend -> Redis
# Message broker -> RabbitMQ


app = Celery('topics',
             backend=CELERY_RESULT_BACKEND,
             broker=CELERY_BROKER_URL,
             timezone='PDT'
            )

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)


app.conf.beat_schedule = {
    'add-every-31-seconds': {
        'task': 'topics.tasks.add',
        'schedule': 30.0, # 30 seconds
        'args': (11, 16)
    },
    'notify_user_of_new_topic': {
        'task': 'topics.tasks.notify_user_of_new_topic',
        'schedule': 60*60*24, # Once a day
        'args': ()
    },
    'import_reddit_topics': {
        'task': 'topics.tasks.import_reddit_topics',
        'schedule': 60*60*24, # Once a day
        'args': ()
    },
}

app.conf.timezone = 'UTC'
app.autodiscover_tasks()

app.config_from_object(settings, namespace='CELERY')

if __name__ == '__main__':
    app.start()