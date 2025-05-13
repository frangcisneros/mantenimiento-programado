from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..services import PiezasService, MaquinasService
from ..models import Maquina, Pieza, Mantenimiento, Encargado, Tarea, PiezasUtilizadas
from ..serializers import (
    MaquinaSerializer,
    PiezaSerializer,
    EncargadoSerializer,
    MantenimientoSerializer,
    TareaSerializer,
    PiezasUtilizadasSerializer,
)


class MaquinaViewSet(viewsets.ModelViewSet):
    queryset = Maquina.objects.all()
    # este serializer se utiliza para validar los datos
    serializer_class = MaquinaSerializer


class PiezaViewSet(viewsets.ModelViewSet):
    queryset = Pieza.objects.all()
    serializer_class = PiezaSerializer


class EncargadoViewSet(viewsets.ModelViewSet):
    queryset = Encargado.objects.all()
    serializer_class = EncargadoSerializer


class MantenimientoViewSet(viewsets.ModelViewSet):
    queryset = Mantenimiento.objects.all()
    serializer_class = MantenimientoSerializer


class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer


class PiezasUtilizadasViewSet(viewsets.ModelViewSet):
    queryset = PiezasUtilizadas.objects.all()
    serializer_class = PiezasUtilizadasSerializer
