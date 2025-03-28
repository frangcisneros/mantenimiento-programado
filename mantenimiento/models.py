from typing import Any
from django.db import models


class Maquina(models.Model):
    id_maquina = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    id_ultima_tarea = models.ForeignKey(
        "TareaMantenimiento",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="ultima_tarea_maquina",
    )


class TareaMantenimiento(models.Model):
    id_tarea = models.AutoField(primary_key=True)
    id_tipo_mantenimiento = models.ForeignKey(
        "TipoMantenimiento",
        on_delete=models.CASCADE,
        related_name="tareas_mantenimiento",
    )
    id_maquina = models.ForeignKey(
        "Maquina",
        on_delete=models.CASCADE,
        related_name="tareas_maquina",
    )
    id_pieza = models.ForeignKey(
        "Pieza",
        on_delete=models.CASCADE,
        related_name="tareas_pieza",
    )
    id_encargado = models.ForeignKey(
        "Encargado",
        on_delete=models.CASCADE,
        related_name="tareas_encargado",
    )
    fecha = models.DateField()


class Pieza(models.Model):
    id_pieza = models.AutoField(primary_key=True)
    id_maquina = models.ForeignKey(
        "Maquina",
        on_delete=models.CASCADE,
        related_name="pieza_maquina",
    )


class TipoMantenimiento(models.Model):
    id_tipo_mantenimiento = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)


class Encargado(models.Model):
    id_encargado = models.AutoField(primary_key=True)
