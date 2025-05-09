from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..services.piezas_service import PiezasService
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


class UsarPiezaAPIView(APIView):
    def post(self, request, format=None):
        id_pieza = request.data.get("id_pieza")
        cantidad = request.data.get("cantidad")
        id_tarea = request.data.get("id_tarea")

        # Validar que se hayan enviado los datos necesarios
        if not all([id_pieza, cantidad, id_tarea]):
            return Response(
                {"detail": "Faltan datos requeridos (id_pieza, cantidad, id_tarea)"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            service = PiezasService()
            service.usar_pieza(id_pieza, int(cantidad), int(id_tarea))
            return Response(
                {"detail": "Pieza utilizada correctamente"}, status=status.HTTP_200_OK
            )
        except ValueError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Pieza.DoesNotExist:
            return Response(
                {"detail": "La pieza no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            # Para depuración, podrías imprimir el error o registrarlo.
            return Response(
                {"detail": "Error interno"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
