from django import forms
from .models import Cat, Pyme, Producto


class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ['nombre', 'descripcion']

        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),

        }

class PymeForm(forms.ModelForm):
    class Meta:
        model = Pyme
        fields = ['nombre', 'rut_empresa', 'direccion', 'cat', 'img']

        labels = {
            'nombre': 'Nombre',
            'rut_empresa': 'Rut de Empresa',
            'direccion': 'Dirección',
            'cat': 'Categoría de la '

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),

        }
