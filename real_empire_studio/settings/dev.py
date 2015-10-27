from .base import *

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'realempire_db',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'realempire',
        'HOST': '127.0.0.1'
    }
}

ALLOWED_HOSTS = ['*']

DEBUG = True

SECRET_KEY = 'test'

INSTALLED_APPS += (
    'autofixture',
    'debug_toolbar',
    'django_extensions',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
