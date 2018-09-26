"""
Django settings for commgen project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from .config import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gy)8sr$20%yzfqo**id!p0)&qe=6+x)&w3+07jfre&8-0tv1^3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
# SMTP settings
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = CONFIG_EMAIL_HOST
EMAIL_USE_TLS = CONFIG_EMAIL_USE_TLS 
EMAIL_PORT = CONFIG_EMAIL_PORT
EMAIL_HOST_USER = CONFIG_EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = CONFIG_EMAIL_HOST_PASSWORD 
# EMAIL_HOST = 'smtp.live.com'
# EMAIL_HOST_USER = 'bhavya.92@hotmail.com'
# EMAIL_HOST_PASSWORD = '!123bhavya'
# EMAIL_PORT = '25'

LOGIN_REDIRECT_URL = '/dashboard/'

# Application definition

AUTH_USER_MODEL = 'users.User'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'language_flags'
    # 'debug_toolbar',
    'schedule',
    'myapp',
    # 'templatetags',
    'users',
    'mailing_list',
    'mailing_templates',
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # 'django.template.context_processors.i18n',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',

]

ROOT_URLCONF = 'commgen.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'commgen.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql', 
    #     'NAME': 'dummy',
    #     'USER': 'root',
    #     'PASSWORD': '!1bhavya',
    #     'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
    #     'PORT': '3306',
    # },
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

####################################
    ##  CKEDITOR CONFIGURATION ##
####################################

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}

###################################


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGES = [
    ('en','English'),
    ('fr','French'),
    ('fi','Finnish'),
]

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
CRISPY_TEMPLATE_PACK = 'bootstrap3'
if DEBUG:
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(BASE_DIR,'static','static-only')
    MEDIA_ROOT = os.path.join(BASE_DIR,'media/')
    STATICFILES_DIRS = (os.path.join(BASE_DIR,'static','static'),)
    CKEDITOR_UPLOAD_PATH = 'uploads/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)