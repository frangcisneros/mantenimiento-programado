from .base import *

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        # TODO: CREAR UNA TABLA PARA DEVELOPMENT
        "NAME": "mantenimiento_db",
        "USER": "admin_mantenimiento",
        "PASSWORD": "admin_mantenimiento",
        "HOST": "db",
        "PORT": "5432",
    }
}

# ? QUE ES ESTO?
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

INSTALLED_APPS += [
    "debug_toolbar",
]
MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
