"""
Django settings for EC project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-b962od5lzgau+yfd@u4k^6v2x_+8$ta*!n62mqy$r8430ln+q#"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 自定义Apps
    "Apps.accounts.apps.AccountsConfig",
    "Apps.activities.apps.ActivitiesConfig",
    "Apps.admin_panel.apps.AdminPanelConfig",
    "Apps.feedback.apps.FeedbackConfig",
    "Apps.forum.apps.ForumConfig",
    "Apps.learning.apps.LearningConfig",
    "Apps.mystery_hunt.apps.MysteryHuntConfig",
    "Apps.settings.apps.SettingsConfig",
    "Apps.socialize.apps.SocializeConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "EC.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [Path.joinpath(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = "EC.wsgi.application"


# 这里设置MEDIA相关内容
MEDIA_ROOT = Path.joinpath(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "ec",
        'USER': 'root',
        'PASSWORD': 'Scs31410.0',
        'HOST': '127.0.0.1',       # 主机
        'PORT': '3306',     # 端口
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"


STATICFILES_DIRS = [
    Path.joinpath(BASE_DIR, 'static'),                  # 项目的全局静态文件目录
    Path.joinpath(BASE_DIR, 'Apps/accounts/static'),    # 应用程序 accounts 的静态文件目录
    # 添加其他应用程序的静态文件目录，如果有的话
]


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 发送邮箱验证码
EMAIL_HOST = "smtp.163.com"
EMAIL_PORT = 25
EMAIL_HOST_USER = "ustc_englishclub@163.com"
EMAIL_HOST_PASSWORD = "EIXLAEEAHLNKHMTL"          # 密码 (注意：这里的密码指的是授权码)
EMAIL_USE_TLS = False
EMAIL_FROM = "ustc_englishclub@163.com"

