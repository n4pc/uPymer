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
        fields = ['nombre', 'rut_empresa', 'direccion', 'cat']

        labels = {
            'nombre': 'Nombre',
            'rut_empresa': 'Rut de Empresa',
            'direccion': 'Dirección',
            'cat': 'Categoría de la Pyme'

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'rut_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'cat': forms.Select(attrs={'class': 'form-control'}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'pyme']

        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'pyme': 'Pyme asociada al producto'

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'pyme': forms.Select(attrs={'class': 'form-control'}),
        }
