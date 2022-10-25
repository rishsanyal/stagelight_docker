from __future__ import absolute_import, unicode_literals

from .celery import app
from topics.lib.import_topics import RedditTopicsParser


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


@app.task
def import_reddit_topics():
    parser = RedditTopicsParser()
    parser.parse_and_populate_topics()