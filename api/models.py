from django.db import models


class Maquina(models.Model):
    idMaquina = models.AutoField(primary_key=True)
    tipoMaquina = models.CharField(max_length=100)


class Pieza(models.Model):
    idPieza = models.AutoField(primary_key=True)
    tipoPieza = models.CharField(max_length=100)


# tabla que relaciona muchos a muchos pieza y maquina
class PiezaMaquina(models.Model):
    # no se si hace falta tener un idPiezaMaquina
    idPiezaMaquina = models.AutoField(primary_key=True)
    idPieza = models.ForeignKey(Pieza, on_delete=models.CASCADE)
    idMaquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)


class Mantenimiento(models.Model):
    idMantenimiento = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)


class Encargado(models.Model):
    idEncargado = models.AutoField(primary_key=True)


class Tarea(models.Model):
    idTarea = models.AutoField(primary_key=True)
    idMantenimiento = models.ForeignKey(Mantenimiento, on_delete=models.CASCADE)
    idMaquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    idPieza = models.ForeignKey(Pieza, on_delete=models.CASCADE)
    idEncargado = models.ForeignKey(Encargado, on_delete=models.CASCADE)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
