"""
Django settings for data_collector_service project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
SECRET_KEY = "django-insecure-k^c404!2*woj(h(+ek*e#=0sh^qrjw9y-g34m^*qy=^=!43v%^"
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.getenv("APP_DEBUG")
DEBUG = True

ALLOWED_HOSTS = ["data_collector", "localhost","*"]


# Application definition

INSTALLED_APPS = [
    "django_prometheus",
    "collector",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_prometheus.middleware.PrometheusAfterMiddleware",
]

ROOT_URLCONF = "data_collector_service.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "data_collector_service.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS'),

KAFKA_TOPICS = {
    'trigger-daily': os.getenv('KAFKA_TRIGGER_DAILY'),
    'trigger-15min': os.getenv('KAFKA_TRIGGER_15MIN'),
    'trigger-historical': os.getenv('KAFKA_TRIGGER_HISTORICAL'),

    'daily': os.getenv("KAFKA_DAILY_TOPIC"),
    '15min': os.getenv("KAFKA_15min_TOPIC"),
    'options': os.getenv("KAFKA_OPTION_TOPIC"),
    'historical': os.getenv("KAFKA_HISTORICAL_TOPIC"),
    'task_queue': os.getenv("KAFKA_TASK_TOPIC")
}

TWELVE_DATA_API_KEYS = [os.getenv("TWELVE_DATA_API_1"),
                        os.getenv("TWELVE_DATA_API_2"),
                        os.getenv("TWELVE_DATA_API_3"),
                        os.getenv("TWELVE_DATA_API_4"),
                        os.getenv("TWELVE_DATA_API_5")]

TWELVE_DATA_API_1 = os.getenv("TWELVE_DATA_API_1")
TWELVE_DATA_API_2 = os.getenv("TWELVE_DATA_API_2")
TWELVE_DATA_API_3 = os.getenv("TWELVE_DATA_API_3")
TWELVE_DATA_API_4 = os.getenv("TWELVE_DATA_API_4")
TWELVE_DATA_API_5 = os.getenv("TWELVE_DATA_API_5")
