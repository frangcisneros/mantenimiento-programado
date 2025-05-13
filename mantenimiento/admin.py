from django.contrib import admin
from .models import Maquina, Pieza, Encargado, Mantenimiento, Tarea, PiezasUtilizadas

admin.site.register(Maquina)
admin.site.register(Pieza)
admin.site.register(Encargado)
admin.site.register(Mantenimiento)
admin.site.register(Tarea)
admin.site.register(PiezasUtilizadas)
