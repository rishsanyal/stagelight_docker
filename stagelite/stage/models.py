import django
from django.db import models

from django.contrib.auth.models import User

# 1. Create user

class StageUser(User):
    NOTIFICATION_CHOICES = (
        ('a', 'email'),
        ('b', 'text')
    )
    user_email = models.EmailField(max_length=254, unique=True, default="")
    user_notification_preference = models.CharField(max_length=1, choices=NOTIFICATION_CHOICES, default='a')

    def __str__(self):
        return self.username