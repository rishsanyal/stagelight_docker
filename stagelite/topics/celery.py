from __future__ import absolute_import, unicode_literals
# import settings
# from django.conf import CELERY_RESULT_BACKEND, CELERY_BROKER_URL
from stagelite.settings import CELERY_RESULT_BACKEND, CELERY_BROKER_URL

from celery import Celery

# Result backend -> Redis
# Message broker -> RabbitMQ


app = Celery('topics',
             backend=CELERY_RESULT_BACKEND,
             broker=CELERY_BROKER_URL,
             include=['topics.tasks'],
             timezone='PDT'
            )

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

app.conf.beat_schedule = {
    'tasks.add': {
        'task': 'topics.tasks.add',
        'schedule': 30.0, # Every 30 minutes
        'args': (16, 16)
    },
}

if __name__ == '__main__':
    app.start()