from rest_framework import serializers
from .models import Maquina, TareaMantenimiento, Pieza, TipoMantenimiento, Encargado


class MaquinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquina
        fields = "__all__"


class TareaMantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TareaMantenimiento
        fields = "__all__"


class PiezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pieza
        fields = "__all__"


class TipoMantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMantenimiento
        fields = "__all__"


class EncargadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encargado
        fields = "__all__"
