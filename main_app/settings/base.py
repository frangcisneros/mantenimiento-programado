from pathlib import Path
from decouple import config
import sys

BASE_DIR = Path(__file__).resolve().parent.parent

#! NO SE SI DEJAR ESTO
SECRET_KEY = "django-insecure-vuwpwu1n1gqs6x1tbiji5^b3s)su!ek-h13&@9n4a7!rf^gn&d"

#! NO SE SI DEJAR ESTO
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # * TERCEROS
    "rest_framework",
    # * PROPIOS
    "mantenimiento",
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

ROOT_URLCONF = "main_app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # ? TENGO QUE AGREGAR "[BASE_DIR / "templates"]"?
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

WSGI_APPLICATION = "main_app.wsgi.application"

# * ESTO SE SOBREESCRIBE PARA CADA TIPO DE ENTORNO, VOY A DEJAR EL ORIGINAL PERO COMENTADO
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": config("DB_NAME", default="mantenimiento_db"),
#         "USER": config("DB_USER", default="admin_mantenimiento"),
#         "PASSWORD": config("DB_PASSWORD", default="admin_mantenimiento"),
#         "HOST": "db",
#         "PORT": config("DB_PORT", default="5432"),
#     }
# }

DATABASES = {}

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

LANGUAGE_CODE = "es-es"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"

# ! NO SE SI DEJAR ESTO
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
