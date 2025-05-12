from django import forms
from .models import Maquina, OpcionesMaquina, Mantenimiento
from .services import TipoMaquinaService, MantenimientoService, IntervaloService


class MaquinaForm(forms.ModelForm):
    tipo_maquina = forms.ModelChoiceField(
        queryset=TipoMaquinaService().obtener_tipos_maquina(),
        label="Tipo de Máquina",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    class Meta:
        model = Maquina
        fields = ["tipo_maquina"]


class TareaForm(forms.ModelForm):
    # * tipo de mantenimiento se refiere al modelo "Mantenimiento" no al modelo "OpcionesMantenimiento"
    tipo_mantenimiento = forms.ModelChoiceField(
        queryset=MantenimientoService().obtener_mantenimientos(),
        label="Tipo de Mantenimiento",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    class Meta:
        model = Maquina
        fields = ["tipo_mantenimiento"]


class MantenimientoForm(forms.ModelForm):
    tipo_mantenimiento = forms.ModelChoiceField(
        queryset=MantenimientoService().obtener_tipos_mantenimiento(),
        label="Tipo de Mantenimiento",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    intervalo = forms.ModelChoiceField(
        queryset=IntervaloService().obtener_intervalos(),
        label="Intervalo de Mantenimiento",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    parte_maquina = forms.CharField(
        label="Parte de la Máquina",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    instrucciones = forms.CharField(
        label="Instrucciones",
        widget=forms.Textarea(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Mantenimiento
        fields = ["tipo_mantenimiento", "intervalo", "parte_maquina", "instrucciones"]
