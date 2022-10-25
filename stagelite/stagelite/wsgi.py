"""
WSGI config for stagelite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stagelite.settings')

application = get_wsgi_application()



# from django.contrib.auth.models import User
from stage.models import StageUser

u, _ = StageUser.objects.get_or_create(username='test_user')
u.user_email = "rsanyal@ucdavis.edu"
u.set_password('password')
u.is_superuser = True
u.is_staff = True
u.save()
