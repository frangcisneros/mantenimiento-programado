from django import forms
from .models import (
    Maquina,
    OpcionesMaquina,
    Mantenimiento,
    OpcionesMantenimiento,
    OpcionesIntervalo,
    Encargado,
    Tarea,
)
from .services import (
    TipoMaquinaService,
    MantenimientoService,
    IntervaloService,
    EncargadoService,
    MaquinasService,
    EncargadoService,
)


class CodigoForm(forms.Form):
    codigo = forms.CharField(max_length=50, label="Código")


class TipoMaquinaForm(forms.ModelForm):
    tipo_maquina = forms.CharField(
        label="Crear tipo de máquina",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = OpcionesMaquina
        fields = ["tipo_maquina"]


class IntervaloForm(forms.ModelForm):
    intervalo = forms.CharField(
        label="Crear Intervalo",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = OpcionesIntervalo
        fields = ["intervalo"]


class TipoMantenimientoForm(forms.ModelForm):
    tipo_mantenimiento = forms.CharField(
        label="Crear tipo de mantenimiento",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = OpcionesMantenimiento
        fields = ["tipo_mantenimiento"]


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
    id_mantenimiento = forms.ModelChoiceField(
        queryset=MantenimientoService().obtener_mantenimientos(),
        label="Mantenimiento",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    id_encargado = forms.ModelChoiceField(
        queryset=EncargadoService().obtener_encargados(),
        label="Encargado",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    id_maquina = forms.ModelChoiceField(
        queryset=MaquinasService().obtener_maquinas(),
        label="Máquina",
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    fecha_inicio = forms.DateField(
        label="Fecha de Inicio",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )
    fecha_fin = forms.DateField(
        label="Fecha de Fin",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
    )

    class Meta:
        model = Tarea
        fields = [
            "id_mantenimiento",
            "id_encargado",
            "id_maquina",
            "fecha_inicio",
            "fecha_fin",
        ]


class EncargadoForm(forms.ModelForm):
    nombre = forms.CharField(
        label="Nombre",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    apellido = forms.CharField(
        label="Apellido",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    telefono = forms.CharField(
        label="Teléfono",
        max_length=15,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Encargado
        fields = ["nombre", "apellido", "telefono"]


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
