from .base import *

DEBUG = True  # Se suele dejar DEBUG=False en staging para simular producción
ALLOWED_HOSTS = ["*"]  # O la IP correspondiente de tu LAN

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mantenimiento_db_dev",
        "USER": "admin_dev",
        "PASSWORD": "admin_dev",
        "HOST": "db_staging",  # Conecta al contenedor db_staging
        "PORT": "5432",
    }
}

# ? QUE ES ESTO?
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

# INSTALLED_APPS += [
#     "debug_toolbar",
# ]
# MIDDLEWARE += [
#     "debug_toolbar.middleware.DebugToolbarMiddleware",
# ]
