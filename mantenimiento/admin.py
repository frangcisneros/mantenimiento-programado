from django.contrib import admin

# Register your models here.

from .models import Maquina, TareaMantenimiento

admin.site.register(Maquina)
admin.site.register(TareaMantenimiento)
