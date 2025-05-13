from django.db import models


class tipoPieza(models.Model):
    id_tipo_pieza = models.AutoField(primary_key=True)
    tipo_pieza = models.CharField(max_length=100)


# * este modelo indica cada pieza individual
class Pieza(models.Model):
    id_pieza = models.AutoField(primary_key=True)
    # * el tipo_pieza indica el tipo de pieza, este debe ser una selección entre ciertas opciones
    tipo_pieza = models.ForeignKey(tipoPieza, on_delete=models.CASCADE)
    # TODO: deberia haber mas campos dependiendo el tipo de pieza, por ejemplo para aceites el tipo de aceite, para rodamientos el diametro y tipo, etc.
    # ? deberia haber una tabla de inventarios? una tabla para cada tipo de pieza? o una tabla general de piezas?
    cantidad = models.IntegerField()


class OpcionesMaquina(models.Model):
    id_opcion_maquina = models.AutoField(primary_key=True)
    tipo_maquina = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_maquina


class Maquina(models.Model):
    id_maquina = models.AutoField(primary_key=True)
    tipo_maquina = models.ForeignKey(OpcionesMaquina, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo_maquina.tipo_maquina


# * clase opciones de mantenimiento que permite que luego podamos seleccionarlas desde la clase mantenimiento, para no hardcodear los tipos de mantenimiento
class OpcionesMantenimiento(models.Model):
    id_opcion_mantenimiento = models.AutoField(primary_key=True)
    tipo_mantenimiento = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_mantenimiento


class OpcionesIntervalo(models.Model):
    id_opcion_intervalo = models.AutoField(primary_key=True)
    intervalo = models.CharField(max_length=100)

    def __str__(self):
        return self.intervalo


# * la clase mantenimiento describe el tipo de mantenimiento, este despues puede ser asignado a una tarea
class Mantenimiento(models.Model):
    id_mantenimiento = models.AutoField(primary_key=True)
    # * el intervalo dicta cada cuanto se hace el mantenimiento
    intervalo = models.ForeignKey(OpcionesIntervalo, on_delete=models.CASCADE)
    # TODO: agregar un modelo para seleccionar las partes de la maquina
    parte_maquina = models.CharField(max_length=100)
    # * tipo_mantenimiento dicta el tipo de mantenimiento que se debe hacer, en este caso si es una lista de opciones, las cuales podrian ser editadas
    tipo_mantenimiento = models.ForeignKey(
        OpcionesMantenimiento, on_delete=models.CASCADE
    )
    instrucciones = models.TextField()

    def __str__(self):
        return self.tipo_mantenimiento.tipo_mantenimiento

    def mostrar_mantenimiento(self):
        return f"{self.tipo_mantenimiento} - {self.parte_maquina} - {self.instrucciones} - {self.intervalo}"


class Encargado(models.Model):
    id_encargado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, default="Nombre Desconocido")
    apellido = models.CharField(max_length=100, default="Apellido Desconocido")
    telefono = models.CharField(max_length=15, default="Telefono Desconocido")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class PiezasUtilizadas(models.Model):
    id_piezas_utilizadas = models.AutoField(primary_key=True)
    pieza = models.ForeignKey(Pieza, on_delete=models.CASCADE)
    # * la tarea en la que se utilizo la pieza, por lo tanto es una foreign key a la tabla tarea
    id_tarea = models.ForeignKey("Tarea", on_delete=models.CASCADE)
    # * cantidad de la pieza utilizada
    cantidad = models.IntegerField()


# * la clase tarea es el corazon del sistema, es el que se encarga de toda la logica del mantenimiento, a esta se la adjuntan los mantenimientos, las piezas a cambiar y el encargado que lo realiza
class Tarea(models.Model):
    id_tarea = models.AutoField(primary_key=True)
    # * las piezas cambiadas van a estar indicadas en la tabla de PiezasUtilizadas, por lo tanto no es necesario tener un campo en la tabla tarea
    id_mantenimiento = models.ForeignKey(Mantenimiento, on_delete=models.CASCADE)
    id_encargado = models.ForeignKey(Encargado, on_delete=models.CASCADE)
    id_maquina = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    # * las fechas tambien debe incluir la hora para poder calcular la duracion de la tarea
    # * las fechas permiten colocar valores a futuro, por lo que no es necesario tener un campo que indique el estado de la tarea
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
