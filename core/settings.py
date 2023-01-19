# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, environ
import django_heroku
import dj_database_url
from decouple import config

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', default='S#perS3crEt_007000123456789')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

# Assets Management
ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')

# load production server from .env
ALLOWED_HOSTS        = ['localhost', 'localhost:85', '127.0.0.1',               env('SERVER', default='127.0.0.1'), '192.168.0.41',
                        'jewelry-creations-studio.herokuapp.com' ]
CSRF_TRUSTED_ORIGINS = ['http://localhost:85', 'http://127.0.0.1', 'https://' + env('SERVER', default='127.0.0.1') , '192.168.0.41',
                        'jewelry-creations-studio.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'embed_video',
    'apps.home'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = "home"  # Route defined in home/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in home/urls.py
TEMPLATE_DIR = os.path.join(CORE_DIR, "apps/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.context_processors.cfg_assets_root',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if os.environ.get('DB', '') == 'SQLITE':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('DATABASE_NAME', ''),
            'USER': os.environ.get('DATABASE_USER', ''),
            'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
            'HOST': os.environ.get('DATABASE_HOST', ''),
            'PORT': os.environ.get('DATABASE_PORT'),
        }
}

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'MST'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "apps/static/"),
)

STATIC_ROOT = os.path.join(BASE_DIR, "apps/static")

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

WAX_CONVERSIONS = {
    'silver': 10.36,
    '10ky': 11.60,
    '14ky': 13.08,
    '18ky': 15.60,
    '10kw': 11.20,
    '14kw': 12.65,
    '18kw': 14.65
}

METAL_PRICES = {
    'silver': 1,
    '10k': 50,
    '14k': 70,
    '18k': 90
}


#############################################################
#############################################################

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())