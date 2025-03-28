from django.db import models


class TipoMantenimiento(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion


class Encargado(models.Model):
    # Agregamos un campo "nombre" para identificar al encargado.
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Maquina(models.Model):
    # Django crea automáticamente un campo "id" si no defines uno.
    # Si necesitas un nombre específico, puedes declararlo así:
    id_maquina = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    # Renombramos el campo a "ultima_tarea" para indicar la relación.
    ultima_tarea = models.ForeignKey(
        "TareaMantenimiento",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="maquinas_con_ultima_tarea",
    )

    def __str__(self):
        return f"Maquina {self.id_maquina} - {self.tipo}"


class Pieza(models.Model):
    id_pieza = models.AutoField(primary_key=True)
    # Relación a Maquina: renombramos el campo a "maquina".
    maquina = models.ForeignKey(
        Maquina, on_delete=models.CASCADE, related_name="piezas"
    )

    def __str__(self):
        return f"Pieza {self.id_pieza} de {self.maquina}"


class TareaMantenimiento(models.Model):
    id_tarea = models.AutoField(primary_key=True)
    # Renombramos campos para que representen claramente la relación
    tipo_mantenimiento = models.ForeignKey(
        TipoMantenimiento, on_delete=models.CASCADE, related_name="tareas"
    )
    maquina = models.ForeignKey(
        Maquina, on_delete=models.CASCADE, related_name="tareas"
    )
    pieza = models.ForeignKey(Pieza, on_delete=models.CASCADE, related_name="tareas")
    encargado = models.ForeignKey(
        Encargado, on_delete=models.CASCADE, related_name="tareas"
    )
    fecha = models.DateField()

    def __str__(self):
        return f"Tarea {self.id_tarea} en {self.maquina} el {self.fecha}"
