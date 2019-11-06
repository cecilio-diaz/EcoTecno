import os
import datetime
from   decouple import config
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = "/media/"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0k^k))ac-zp$6)6f+bljru0e-!fx175hanut(93_5l*t2(@3@1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True       

ALLOWED_HOSTS = ['*']

TIME_ZONE     = 'Europe/Rome'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_beat',
    'django_celery_results',
    'rest_framework',
    'scripts',
    'apps.location',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mt_connect_app_dj.urls'
# Backup de datos
# 1. Start a Celery worker service (specify your Django project name):
#  celery -A mt_connect_app_dj worker -l info -P eventlet
# 2.
# celery -A mt_connect_app_dj beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

# Celery application definition
# https://www.codingforentrepreneurs.com/blog/celery-redis-django
# http://www.programmersought.com/article/5508334793/
# pip install eventlet
# celery -A mt_connect_app_dj worker -l info -P eventlet
# Paros programados
# celery -A mt_connect_app_dj beat -l info -S django

#CELERY_IMPORTS           =("mt_connect_app_dj","apps.ciclos",)
# django-celery
# celery==4.0.0
# django-celery==3.1.17

# Tareas Programadas
# // Tareas Programadas


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    # pip install django-filter
     }

# // CONFIGURAR APIS.
#  // Backup de datos

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mt_connect_app_dj.wsgi.application'


DATABASES = {
        'default': dj_database_url.config(default=config('DB_URL')
        ),
        'redis': dj_database_url.config(default=config('DB_URL_REDIS')
        ),
    }

# celery -A mt_connect_app_dj beat --loglevel=debug --scheduler django_celery_beat.schedulers:DatabaseScheduler
# celery -A mt_connect_app_dj worker -l info -P eventlet

DATOS_CONFIG                = DATABASES['redis']
HOST_REDIS                  = DATOS_CONFIG['HOST']  # Utilizar el mismo puerto de la base de datos para leer redis
PORT_REDIS                  = DATOS_CONFIG['PORT']
CELERY_BROKER_URL           = 'redis://'+str(HOST_REDIS)+':'+str(PORT_REDIS)
CELERY_RESULT_BACKEND       = 'redis://'+str(HOST_REDIS)+':'+str(PORT_REDIS)
CELERY_ACCEPT_CONTENT       = ['application/json']
CELERY_TASK_SERIALIZER      = 'json'
CELERY_RESULT_SERIALIZER    = 'json'
CELERY_TIMEZONE             = TIME_ZONE
CELERY_SEND_TASK_SENT_EVENT = True
CELERY_IMPORTS              = ('mt_connect_app_dj.tasks_maquina',)


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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
USE_I18N      = True
USE_L10N      = True
USE_TZ        = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

#STATIC_ROOT = os.path.join(BASE_DIR,'static')

STATIC_URL = '/static/'

#STATICFILE_DIRS = (os.path.join(BASE_DIR,'static'),)

# CONFITURACTION GUNICORN.
# 1. pip install gunicorn
# 2. gunicorn ems.wsgi:application --bind localhost:8000
