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
