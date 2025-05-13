from django import forms


class CodigoForm(forms.Form):
    codigo = forms.CharField(max_length=50, label="Código")
