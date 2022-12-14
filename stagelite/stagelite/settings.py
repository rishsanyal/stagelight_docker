"""
Django settings for stagelite project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# from celery import app as celery_app

from celery import Celery
from celery.schedules import crontab

app = Celery()
CELERY_IMPORTS = ('topics.tasks',)

CORS_ORIGIN_WHITELIST = [
     'http://localhost:3000',
     'http://0.0.0.0:3000'
     'http://localhost:8000',
     'http://0.0.0.0:8000'
]

# APPEND_SLASH=False

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x=@jj_+jc+crmyb4okgxpb&8zq#z8vkxd63jmh0z#3h19xn+#j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
LOGIN_REDIRECT_URL = "http://127.0.0.1:8000/topics/hello/"

# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_celery_beat',
    # 'celery_admin',
    'stage',
    'topics',
    'django_extensions',
    'django.contrib.admin',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
ROOT_URLCONF = 'stagelite.urls'

CORS_ALLOWED_ORIGINS = [
    "https://domain.com",
    "https://api.domain.com",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:3000",
    "http://0.0.0.0:8000",
    "http://0.0.0.0:3000",
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'stagelite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'stagelite',
#         'USER': 'stagelite',
#         'PASSWORD': 'stagelite',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
    }
}

START_DATABASE = "pg_ctl -D /usr/local/var/postgres start"
STOP_DATABASE = "pg_ctl -D /usr/local/var/postgres stop"


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# SUPERUSER_INFO = {
#     'USERNAME': 'root',
#     'PASSWORD': 'root'
# }


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

### Topics - Settings
REDDIT_KEY = "IuTddFEl2eF_dadQceFmIblq_Ds"
SHELL_PLUS = "ipython"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CELERY_BROKER_URL = "redis://redis:6379"
CELERY_RESULT_BACKEND = "redis://redis:6379"

# DJANGO_SU_NAME=test
# DJANGO_SU_EMAIL=admin12@admin.com
# DJANGO_SU_PASSWORD=mypass123

DJANGO_SUPERUSER_USERNAME="testuser"
DJANGO_SUPERUSER_PASSWORD="testpass"
DJANGO_SUPERUSER_EMAIL="admin@admin.com"

# app.conf.beat_schedule = {
#     'add-every-32-seconds': {
#         'task': 'topics.tasks.add',
#         'schedule': 30.0, # 30 seconds
#         'args': (16, 16)
#     },
#     'notify_user_of_new_topic': {
#         'task': 'notify_user_of_new_topic',
#         'schedule': 60*60*24, # Once a day
#         'args': ()
#     },
#     'import_reddit_topics': {
#         'task': 'import_reddit_topics',
#         'schedule': 60*60*24, # Once a day
#         'args': ()
#     },
# }
# app.conf.timezone = 'UTC'
