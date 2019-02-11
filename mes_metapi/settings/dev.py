from .base import *

DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS += ['web']

# Development Apps
INSTALLED_APPS += []

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PWD': config('DB_PWD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT')
    }
}