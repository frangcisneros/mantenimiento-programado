from django.contrib import admin

# Register your models here.

from .models import Maquina, Pieza, Encargado, PiezaMaquina, Mantenimiento, Tarea

admin.site.register(Maquina)
admin.site.register(Pieza)
admin.site.register(Encargado)
admin.site.register(PiezaMaquina)
admin.site.register(Mantenimiento)
admin.site.register(Tarea)
