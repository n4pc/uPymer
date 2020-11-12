from django import forms
from .models import Cat, Pyme, Producto


class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ['nombre', 'descripcion','img']

        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'img' : 'Imágen de Categoría',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PymeForm(forms.ModelForm):
    class Meta:
        model = Pyme
        fields = ['nombre', 'rut_empresa', 'descripcion', 'direccion', 'cat', 'img']

        labels = {
            'nombre': 'Nombre',
            'rut_empresa': 'Rut de Empresa',
            'descripcion': 'Descripción',
            'direccion': 'Dirección',
            'cat': 'Categoría de la Pyme',
            'img' : 'Imágen de Pyme',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'rut_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'cat': forms.Select(attrs={'class': 'form-control'}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'pyme', 'img']

        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'pyme': 'Pyme asociada al producto',
            'img' : 'Imágen del producto',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'pyme': forms.Select(attrs={'class': 'form-control'}),
        }
