"""
Django settings for P_Ndjango project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os, json
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)

secret_file = os.path.join(BASE_DIR, "secrets.json")  # secrets.json 파일 위치를 명시

with open(secret_file) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret("SECRET_KEY")

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(BASE_DIR, "google-credentials.json")

GOOGLE_CLOUD_API_KEY = get_secret("GOOGLE_CLOUD_API_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','localhost', '3.34.134.128']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "account_app",
    "contents_app",
    "social_django",
    "django.contrib.sites",
    "allauth",
    "allauth.socialaccount",
    "django_summernote",
]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = get_secret("GOOGLE_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = get_secret("GOOGLE_SECRET_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI = "http://127.0.0.1:8000/complete/google-oauth2/"
AUTHENTICATION_BACKENDS = (
    "social_core.backends.google.GoogleOAuth2",
    "social_core.backends.naver.NaverOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)
SOCIAL_AUTH_AUTHENTICATION_BACKENDS = [
    "social_core.backends.naver.NaverOAuth2",
    "social_core.backends.google.GoogleOAuth2",
]

# naver social login setting
SOCIAL_AUTH_NAVER_KEY = get_secret("NAVER_KEY")
SOCIAL_AUTH_NAVER_SECRET = get_secret("NAVER_SECRET_KEY")

# login setting
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "main"
SITE_ID = 2

SOCIALACCOUNT_LOGIN_ON_GET = True
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_ON_GET = True

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "P_Ndjango.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "account_app/templates")],
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

WSGI_APPLICATION = "P_Ndjango.wsgi.application"

# AWS S3 셋팅
AWS_REGION = "ap-northeast-2"
AWS_STORAGE_BUCKET_NAME = get_secret("BUCKET_NAME")
AWS_ACCESS_KEY_ID = get_secret("ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = get_secret("SECRET_ACCESS_KEY")
AWS_S3_CUSTOM_DOMAIN = "%s.s3.%s.amazonaws.com" % (AWS_STORAGE_BUCKET_NAME, AWS_REGION)
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
print(AWS_S3_CUSTOM_DOMAIN)

# Static Setting
# python manage.py collectstatic
STATIC_URL = "http://%s/static/" % AWS_S3_CUSTOM_DOMAIN
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "P_Ndjango\static\css"),
#     os.path.join(BASE_DIR, "P_Ndjango\static\js"),
#     os.path.join(BASE_DIR, "P_Ndjango\static\summernote"),
# ]

# Media Setting
MEDIA_URL = "http://%s/media/" % AWS_S3_CUSTOM_DOMAIN

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

DJANGO_SUMMERNOTE_CONFIG = {
    "summernote": {
        "width": "100%",
        "height": "480",
        "upload_attachment_to": "media/uploads/",
    },
}
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": get_secret("NAME"),
        "USER": get_secret("USER"),
        "PASSWORD": get_secret("PASSWORD"),
        "HOST": get_secret("HOST"),
        "PORT": get_secret("PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Seoul"  # 데이터베이스 시간대

USE_I18N = True  # 장고 번역시스템 활성화 여부
USE_L10N = True  # 현지화 데이터 형식 사용 여부
USE_TZ = False  # 시간대 인식 여부


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# X_FRAME_OPTIONS = 'SAMEORIGIN'
