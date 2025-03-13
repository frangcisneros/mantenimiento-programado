from typing import Any
from django.db import models


class Maquina(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.nombre


class TareaMantenimiento(models.Model):
    maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    fecha_programada = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return f"Mantenimiento de {self.maquina} en {self.fecha_programada}"
