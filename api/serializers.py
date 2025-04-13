from rest_framework import serializers
from .models import Maquina, Pieza, Encargado, Mantenimiento, Tarea, PiezasUtilizadas


class MaquinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquina
        fields = "__all__"


class PiezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pieza
        fields = "__all__"


class EncargadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encargado
        fields = "__all__"


class PiezasUtilizadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiezasUtilizadas
        fields = "__all__"


class MantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantenimiento
        fields = "__all__"


class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = "__all__"
