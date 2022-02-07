"""
Django settings for Codeshare project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import django_heroku
from pathlib import Path
import os

# fromd decouple im

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n&@t3_(te+%ct#timl#oingcijh(2k6wc2miy!#ns-acq2c)%-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# DJANGO_SETTINGS_MODULE = config.settings.production

ALLOWED_HOSTS = [
    '326e-2405-204-30af-a836-79ff-e0e3-b06b-2c5d.ngrok.io',
    '127.0.0.1',
    'codescape006.herokuapp.com'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Main.apps.MainConfig',
    'django.contrib.sites',
    'accounts.apps.AccountsConfig',
    'chat',
    'channels',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
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

ROOT_URLCONF = 'Codeshare.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'Templates')],
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

WSGI_APPLICATION = 'Codeshare.wsgi.application'
ASGI_APPLICATION = 'chat.asgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'Codeshare',
    #     'USER': 'postgres',
    #     'PASSWORD': 'nitish',
    #     'HOST': 'localhost'
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd5gd69qgj9meb1',
        'USER': 'jlbztgzfojgidw',
        'PASSWORD': '1e03cd5e50fd95f518f8c9e9578311a61ceedb40ed251ac07969e893e655e0e6',
        'HOST': 'ec2-54-235-98-1.compute-1.amazonaws.com',
        'PORT':'5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS =[
#     os.path.join(BASE_DIR,'static')
# ]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'
django_heroku.settings(locals())
AUTHENTICATION_BACKEND = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]
SOCIALACCOUNT_PROVIDERS = {
    'google':{
        'SCOPE':[
            'profile',
            'email',
            
        ],
        'AUTH_PARAMS':{
            'access_type':'online',
        }
    }
}   

SITE_ID = 4
LOGIN_REDIRECT_URL = '/'
# SIGNUP_REDIRECT_URL = '/welcome'
LOGOUT_DIRECT_URL = '/'
LOGIN_URL = '/accounts/login'
ACCOUNT_SIGNUP_REDIRECT_URL = "/welcome"

CHANNEL_LAYERS = {
    'default':{
        'BACKEND':'channels.layers.InMemoryChannelLayer',
    }
}   