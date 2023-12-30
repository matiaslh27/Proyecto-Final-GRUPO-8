from .base import *

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'matiaslh27$blog_db',
        'USER': 'matiaslh27',
        'PASSWORD': 'guitargeorge',
        'HOST': 'matiaslh27.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

STATIC_ROOT= BASE_DIR/'staticfiles'