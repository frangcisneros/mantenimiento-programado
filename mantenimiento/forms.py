from django import forms
from .models import Maquina, OpcionesMaquina
from .services import TipoMaquinaService


class MaquinaForm(forms.ModelForm):
    tipo_maquina = forms.ModelChoiceField(
        queryset=TipoMaquinaService().obtener_tipos_maquina(),
        label="Tipo de Máquina",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    class Meta:
        model = Maquina
        fields = ["tipo_maquina"]
