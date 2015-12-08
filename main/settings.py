"""Common settings and globals."""

import os
import socket

import dj_database_url


# ######### SETTINGS
ALLOWED_HOSTS = [
    'localhost',
    'fractionsaseasyasxyz.herokuapp.com',
    'www.fractionsaseasyas.xyz',
]
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRODUCTION = os.getenv('PRODUCTION', False)
ROOT_DIR = os.path.dirname(BASE_DIR)
ROOT_URLCONF = 'main.urls'
SECRET_KEY = 'rm6%rrzy6d$$3cp0^x*av9w$1^4&w#sod=6#1(9@)aykzl5qhf'
SITE_ID = 1
WSGI_APPLICATION = 'main.wsgi.application'


# ######### AUTHENTICATION CONFIGURATION
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)


# ######### DATABASE CONFIGURATION
if PRODUCTION:
    DATABASES = {}
    DATABASES['default'] = dj_database_url.config()
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'fractions',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }


# ######### DEBUG CONFIGURATION
DEBUG = not PRODUCTION


# ######### HOST VARIABLES
hostname = socket.gethostname()
hostname = hostname.split('.')[0] if '.' in hostname else hostname


# ######### INSTALLED APPS CONFIGURATION
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'django_extensions',
]

LOCAL_APPS = [
    'main',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# ######### INTERNATIONALIZATION CONFIGURATION
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# ######### LOGGING CONFIGURATION
LOGGING = {
    'disable_existing_logging': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(filename)s \t %(funcName)s:%(lineno)d \t %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'level': 'DEBUG',
        },
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'formatter': 'verbose',
            'level': 'ERROR',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
        'propagate': False,
    },
    'version': 1,
}


# ######### MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]


# ######### STATIC CONFIGURATION
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# ######### TEMPLATE CONFIGURATION
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
