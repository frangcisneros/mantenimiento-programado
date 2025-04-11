from rest_framework import viewsets
from .models import Maquina, Pieza, PiezaMaquina, Mantenimiento, Encargado, Tarea
from .serializers import (
    MaquinaSerializer,
    PiezaSerializer,
    EncargadoSerializer,
    PiezaMaquinaSerializer,
    MantenimientoSerializer,
    TareaSerializer,
)


class MaquinaViewSet(viewsets.ModelViewSet):
    queryset = Maquina.objects.all()
    # este serializer se utiliza para validar los datos
    serializer_class = MaquinaSerializer


class PiezaViewSet(viewsets.ModelViewSet):
    queryset = Pieza.objects.all()
    serializer_class = PiezaSerializer


class PiezaMaquinaViewSet(viewsets.ModelViewSet):
    queryset = PiezaMaquina.objects.all()
    serializer_class = PiezaMaquinaSerializer


class EncargadoViewSet(viewsets.ModelViewSet):
    queryset = Encargado.objects.all()
    serializer_class = EncargadoSerializer


class MantenimientoViewSet(viewsets.ModelViewSet):
    queryset = Mantenimiento.objects.all()
    serializer_class = MantenimientoSerializer


class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
