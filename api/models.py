from django.db import models


# * este modelo indica cada pieza individual
class Pieza(models.Model):
    id_pieza = models.AutoField(primary_key=True)
    # * el tipo_pieza indica el tipo de pieza, este debe ser una selección entre ciertas opciones
    TIPO_CHOICES = [
        ("rodamiento", "Rodamiento"),
        ("aceite", "Aceite"),
        ("tornillo", "Tornillo"),
        ("correa", "Correa"),
        ("filtro", "Filtro"),
    ]
    tipo_pieza = models.CharField(max_length=20, choices=TIPO_CHOICES)
    # TODO: deberia haber mas campos dependiendo el tipo de pieza, por ejemplo para aceites el tipo de aceite, para rodamientos el diametro y tipo, etc.
    # ? deberia haber una tabla de inventarios? una tabla para cada tipo de pieza? o una tabla general de piezas?
    cantidad = models.IntegerField()


class Maquina(models.Model):
    id_maquina = models.AutoField(primary_key=True)
    tipo_maquina = models.CharField(max_length=100)
    piezas = models.ManyToManyField(Pieza)


# * la clase mantenimiento describe el tipo de mantenimiento, este despues puede ser asignado a una tarea
class Mantenimiento(models.Model):
    id_mantenimiento = models.AutoField(primary_key=True)
    # * el intervalo dicta cada cuanto se hace el mantenimiento
    INTERVALO_CHOICES = [
        ("semanal", "Semanal"),
        ("mensual", "Mensual"),
        ("trimestral", "Trimestral"),
        ("semestral", "Semestral"),
        ("anual", "Anual"),
    ]
    intervalo = models.CharField(max_length=20, choices=INTERVALO_CHOICES)
    # * parte_maquina dicta donde se debe hacer el mantenimiento, en este caso es un campo de texto pero podria tener un modelo en el cual se selecciona la parte de la maquina
    parte_maquina = models.CharField(max_length=100)
    # * tipo_mantenimiento dicta el tipo de mantenimiento que se debe hacer, en este caso si es una lista de opciones, las cuales podrian ser editadas
    TIPO_CHOICES = [
        ("lubricar", "Lubricar"),
        ("pruebas", "Pruebas"),
        ("inspeccion", "Inspección"),
        ("reajuste", "Reajuste"),
    ]
    tipo_mantenimiento = models.CharField(max_length=20, choices=TIPO_CHOICES)
    instrucciones = models.TextField()


class Encargado(models.Model):
    id_encargado = models.AutoField(primary_key=True)


class PiezasUtilizadas(models.Model):
    id_piezas_utilizadas = models.AutoField(primary_key=True)
    # * la pieza utilizada es una pieza que se utiliza en el mantenimiento, por lo tanto es una foreign key a la tabla pieza
    id_pieza = models.ForeignKey(Pieza, on_delete=models.CASCADE)
    # * la tarea en la que se utilizo la pieza, por lo tanto es una foreign key a la tabla tarea
    id_tarea = models.ForeignKey("Tarea", on_delete=models.CASCADE)


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
