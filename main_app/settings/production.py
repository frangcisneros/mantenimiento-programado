from .base import *
import os

DEBUG = False
ALLOWED_HOSTS = ["*"]  # O el dominio real de la fábrica

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mantenimiento_db_prod",
        "USER": "admin_mantenimiento",
        "PASSWORD": "admin_mantenimiento",
        "HOST": "db_production",  # Conecta al contenedor db_production
        "PORT": "5432",
    }
}

# Configuraciones de seguridad y optimización para producción
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"
