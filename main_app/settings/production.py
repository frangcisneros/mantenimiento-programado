from .base import *
import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = False

# TODO: AGREGAR MIS DOMINIOS PARA PRODUCCION
ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        # TODO: CREAR UNA TABLA PARA PRODUCCION
        "NAME": "mantenimiento_db",
        "USER": "admin_mantenimiento",
        "PASSWORD": "admin_mantenimiento",
        "HOST": "db",
        "PORT": "5432",
    }
}

# ? QUE ES ESTO?
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"
