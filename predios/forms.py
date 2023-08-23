from django import forms
from .models import Predio, Propietario

class PredioForm(forms.ModelForm):
    class Meta:
        model = Predio
        fields = ['nombre_o_Direccion', 'tipo_predio', 'numero_catastral', 'numero_matricula']
class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ['nombre', 'tipo_propietario', 'numero_identificacion', 'tipo_identificacion']