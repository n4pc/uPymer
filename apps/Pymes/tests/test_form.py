from django.test import TestCase
from apps.Pymes.models import Cat
from apps.Pymes.forms import CatForm
import tempfile

class CatFormCase(TestCase):
        
    def test_valid_form(self):
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        cat = Cat.objects.create(nombre="AAA", descripcion="descripcion 1", img=image)
        data = {'nombre': cat.nombre, 'descipcion': cat.descripcion,'img': cat.img, }
        form = CatForm(data=data)
        self.assertTrue(form.is_valid())
        
    def test_invalid_form(self):
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        cat = Cat.objects.create(nombre="", descripcion="descripcion 1", img=image)
        data = {'nombre': cat.nombre, 'descipcion': cat.descripcion,'img': cat.img, }
        form = CatForm(data=data)
        self.assertFalse(form.is_valid())
