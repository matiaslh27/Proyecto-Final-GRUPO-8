from .base import *

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'librito2',
        'USER': 'root',
        'PASSWORD': 'guitargeorge',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
